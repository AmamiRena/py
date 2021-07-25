from abc import ABC
from collections import Iterable
import numpy as np
from scipy.optimize import broyden1
import pandas as pd

class BinomialTree(ABC):
    '''
    n: number of periods
    '''
    def __init__(self,n,q=0.5):
        self.n=n
        self.q=q
        self.tree=np.zeros([self.n+1,self.n+1])

    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,value):
        self._n=value

    @property
    def q(self):
        '''
        probability of going up
        '''
        return self._q
    @q.setter
    def q(self,value):
        self._q=value

    @property
    def tree(self):
        return self._tree
    @tree.setter
    def tree(self,tree):
        self._tree=tree
    
    def printtree(self):
        for i in range(self.n+1):
            print('Period='+str(i))
            print(self.tree[i][:i+1])


class Annuity(object):
    '''
    forward annuity immediate (first paymenet is due after one period)
    p: total payment
    r: annual fixed interest rate
    t: number of years
    is_principal: whether total payment is principal
    is_monthly: whether payment is monthly or annual
    '''
    def __init__(self,p,r,t,is_principal=False,is_monthly=False):
        self.is_monthly=1 if is_monthly else 0
        self.n=t*12 if is_monthly else t
        self.r=r/12 if is_monthly else r
        self.p=p*(1+self.r)**self.n if is_principal else p
    
    @property
    def p(self):
        return self._p
    @p.setter
    def p(self,value):
        self._p=value
    
    @property
    def r(self):
        return self._r
    @r.setter
    def r(self,value):
        self._r=value
    
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,value):
        self._n=value
    
    @property
    def monthly_payment(self):
        if self.is_monthly:
            payment=self.p*self.r/((1+self.r)**self.n-1)
            return payment
        else:
            return 0
    
    @property
    def effective_ann_rate(self):
        '''
        if input r is compounded
        '''
        if self.is_monthly:
            return (1+self.r)**12-1
        else:
            return self.r
    
    def lump_sum(self,rate):
        B=self.monthly_payment

        if isinstance(rate,int) or isinstance(rate,float):
            rate=np.repeat(rate,self.n)
        t=np.arange(1,self.n+1)
        result=B*(1+rate)**(-t)
        return result

#Basic Pricing always go through/rate_model
class StockPricing(BinomialTree):
    '''
    binomial model
    n: number of periods
    S0: initial price
    u: upward drift
    d: downward drift
    c: dividend
    '''
    __doc__+=BinomialTree.__doc__

    def __init__(self,n,S0,u,d,c=0):
        '''
        Initiate
        '''
        super().__init__(n)
        self.S0=S0
        self.u=u
        self.d=d
        self.c=c
        self._constructTree()

    @property
    def S0(self):
        return self._S0
    @S0.setter
    def S0(self,value):
        self._S0=value
    
    @property
    def u(self):
        return self._u
    @u.setter
    def u(self,value):
        self._u=value
    
    @property
    def d(self):
        return self._d
    @d.setter
    def d(self,value):
        self._d=value
    
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self,value):
        self._c=value

    def _constructTree(self):
        for i in range(self.n+1):
            for j in range(i+1):
                price=self.S0*(self.u**j)*(self.d**(i-j))
                self.tree[i,j]=price


class FuturesPricing(BinomialTree):
    '''
    n: number of periods
    q: upward probability
    model: tree
    unpaid_coupon: ...execution after being paid
    '''
    __doc__+=BinomialTree.__doc__
    
    def __init__(self,n,model,q,unpaid_coupon=0):
        super().__init__(n,q)
        self._constructTree(model,unpaid_coupon)
    
    @property
    def price(self):
        return self.tree[0,0]

    def _constructTree(self,model,coupon):
        for i in range(self.n,-1,-1):
            if i==self.n:
                self.tree[i]=model.tree[i,:(i+1)]-coupon
            else:
                for j in range(i+1):
                    cd=self.tree[i+1,j]
                    cu=self.tree[i+1,j+1]
                    self.tree[i,j]=self.q*cu+(1-self.q)*cd

# basically an outer layer
class OptionsPricing(BinomialTree):
    '''
    N: Notional amount
    n: number of periods
    model: tree
    r: interet/rate_model
    q: upward probability
    K: strike price
    is_call: True if call option, False for put option
    is_american: True if american option, False for EU option
    '''
    __doc__+=BinomialTree.__doc__

    def __init__(self,N,n,model,r,q,K,is_call=True,is_american=False):
        '''
        Black Scholes Model
        '''
        super().__init__(n,q)
        self.N=N
        self.K=K
        self.adjuster=1 if is_call else -1
        self.is_american=is_american
        self._early_exercise=[]
        self._constructTree(model,r)

    @property
    def N(self):
        return self._N
    @N.setter
    def N(self,value):
        self._N=value

    @property
    def K(self):
        return self._K
    @K.setter
    def K(self,value):
        self._K=value
    
    @property
    def adjuster(self):
        return self._adjuster
    @adjuster.setter
    def adjuster(self,value):
        self._adjuster=value

    @property
    def is_american(self):
        return self._is_american
    @is_american.setter
    def is_american(self,value):
        self._is_american=value
    
    @property
    def price(self):
        return self.tree[0,0]*self.N
    
    @property
    def early_exercise(self):
        result=[]
        for time,no,early_ex,hold in sorted(self._early_exercise):
            data={
                'Time':time,
                'Current Premium': early_ex,
                'Hold': hold
            }
            result.append(data)
        return result
    

    def _constructTree(self,model,r):

        if isinstance(r,int) or isinstance(r,float):
            rate=np.empty([self.n+1,self.n+1])
            rate.fill(r)
        else:
            rate=r.tree
        
        for i in range(self.n,-1,-1):
            if i==self.n:
                for j in range(i+1):
                    self.tree[i,j]=max(0,self.adjuster*(model.tree[i,j]-self.K))
            else:
                for j in range(i+1):
                    cu=self.tree[i+1,j+1]                        
                    cd=self.tree[i+1,j]
                    hold=(self.q*cu+(1-self.q)*cd)/(1+rate[i,j])
                    early_ex=max(0,self.adjuster*(model.tree[i,j]-self.K))
                    if early_ex>hold:
                        self._early_exercise.append((i,j,early_ex,hold))
                    self.tree[i,j]=max(hold,early_ex) if self.is_american else hold


class BondPricing(BinomialTree):
    '''
    n: number of periods
    F: face value
    q: probability of going up
    u: upward drift
    d: downward drift
    c: coupon rate
    harzard: a,b,recovery_rate
    r: interest rate/rate_model
    '''
    __doc__+=BinomialTree.__doc__

    def __init__(self,n,F,q,r,c=0,hazard=None):
        super().__init__(n,q)
        self.F=F
        self.c=c
        self.r=r
        h,recovery=self._compute_defaults(hazard)
        self._constructTree(r,h,recovery)
    
    @property
    def F(self):
        return self._F
    @F.setter
    def F(self,value):
        self._F=value
    
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self,value):
        self._c=value
    
    @property
    def price(self):
        return self.tree[0,0]
    
    def _compute_defaults(self,hazard):
        '''
        h[i,j]=a*b**(i-j/2)
        '''
        h=np.zeros([self.n+1,self.n+1])
        r=1
        if hazard is not None:
            a=hazard['a']
            b=hazard['b']
            r=hazard['recovery_rate']
            for i in range(self.n+1):
                for j in range(i+1):
                    h[i,j]=a*b**(j-i/2)
        return h,r

    def _constructTree(self,r,h,recovery_rate):
        
        if isinstance(r,int) or isinstance(r,float):
            rate=np.empty([self.n+1,self.n+1])
            rate.fill(r)
        else:
            rate=r.tree
        coupon=self.F*self.c
        self.tree[self.n]=np.repeat(self.F+coupon,self.n+1)
        for i in range(self.n-1,-1,-1):
            for j in range(i+1):
                cd=self.tree[i+1,j]
                cu=self.tree[i+1,j+1]
                non_hazard_price=coupon+(self.q*cu+(1-self.q)*cd)*(1-h[i,j])
                hazard_price=h[i,j]*recovery_rate*self.F
                self.tree[i,j]=(non_hazard_price+hazard_price)/(1+rate[i,j])


class ForwardsPricing(BinomialTree):
    '''
    n: number of periods
    model: BinomialTree
    q: upward probability
    r: interest/rate_model
    unpaid_coupon: ...execution after being paid
    '''
    __doc__+=BinomialTree.__doc__
    def __init__(self,n,model,q,r,unpaid_coupon=0):
        super().__init__(n,q)
        self.r=r
        self._constructTree(model,r,unpaid_coupon)
    
    @property
    def r(self):
        return self._r
    @r.setter
    def r(self,value):
        self._r=value
    
    @property
    def price(self):
        zcb_n=BondPricing(self.n,1,self.q,self.r).price
        return self.tree[0,0]/zcb_n
    
    def _constructTree(self,model,r,coupon):
        if isinstance(r,int) or isinstance(r,float):
            rate=np.empty([self.n+1,self.n+1])
            rate.fill(r)
        else:
            rate=r.tree
        for i in range(self.n,-1,-1):
            if i==self.n:
                self.tree[i]=model.tree[i,:(i+1)]-coupon
            else:
                for j in range(i+1):
                    cu=self.tree[i+1,j+1]
                    cd=self.tree[i+1,j]
                    self.tree[i,j]=(self.q*cu+(1-self.q)*cd)/(1+rate[i,j])


class SwapsPricing(BinomialTree):
    '''
    N: notional amount
    n: number of periods
    q: upward probability
    fixed_r: fixed rate in the contract
    start: priods from the exchange starts
    r: rate_model
    is_long: long/short position
    '''
    __doc__+=BinomialTree.__doc__

    def __init__(self,N,n,q,fixed_r,start,r,is_long):
        super().__init__(n-1,q)
        self.N=N
        self.fixed_r=fixed_r
        self.start=start
        self.r=r
        self.adjuster=1 if is_long else -1
        self._constructTree(r)
    
    @property
    def N(self):
        return self._N
    @N.setter
    def N(self,value):
        self._N=value

    @property
    def fixed_r(self):
        return self._fixed_r
    @fixed_r.setter
    def fixed_r(self,value):
        self._fixed_r=value
    
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self,value):
        self._start=value
    
    @property
    def r(self):
        return self._r
    @r.setter
    def r(self,value):
        self._r=value

    @property
    def adjuster(self):
        return self._adjuster
    @adjuster.setter
    def adjuster(self,value):
        self._adjuster=value
    
    @property
    def price(self):
        return self.tree[0,0]*self.N
    
    def _constructTree(self,r):
        rate=r.tree
        for i in range(self.n,-1,-1):
            if i==self.n:
                self.tree[i]=(rate[i,:(i+1)]-self.fixed_r)*self.adjuster/(rate[i,:(i+1)]+1)
            else:
                for j in range(i+1):
                    cu=self.tree[i+1,j+1]
                    cd=self.tree[i+1,j]
                    value=(self.q*cu+(1-self.q)*cd)/(1+rate[i,j])
                    if i>=self.start-1:
                        pay=((rate[i,j]-self.fixed_r)*self.adjuster)/(1+rate[i,j])
                        value+=pay
                    self.tree[i,j]=value


class CashPricing(BinomialTree):
    '''
    binomial tree model for 1 unit of cash
    ---------
    n: number of periods
    q: float
    r: rate_model
    '''
    def __init__(self,n,q,r):
        super().__init__(n,q)
        self._constructTree(r)
    
    def get_zcb_prices(self):
        return self.tree.sum(axis=1)

    def get_spot_rates(self):
        zcb_price=self.get_zcb_prices()[1:]
        spot_rates=zcb_price**-(1/(np.arange(self.n)+1))-1
        return spot_rates
    
    def _constructTree(self,r):
        rate=r.tree
        self.tree[0,0]=1
        for i in range(1,self.n+1):
            self.tree[i,0]=(1-self.q)*self.tree[i-1,0]/(1+rate[i-1,0])
            self.tree[i,i]=self.q*self.tree[i-1,i-1]/(1+rate[i-1,i-1])
            for j in range(1,i):
                pd=self.tree[i-1,j-1]/(1+rate[i-1,j-1])
                pu=self.tree[i-1,j]/(1+rate[i-1,j])
                self.tree[i,j]=self.q*pd+(1-self.q)*pu

class BDTrate(BinomialTree):
    '''
    black-derman-toy rate on binomial tree
    rate[i,j]=a[i]*exp(b[i]*j),a[i],b[i]
    ---------------
    n: number of periods
    drift: a[i]
    vol: b[i]
    '''
    __doc__+=BinomialTree.__doc__

    def __init__(self,n,drift,vol):
        super().__init__(n-1)
        self.a=drift
        self.b=vol
        self._constructTree()
    
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self,value):
        if isinstance(value,int) or isinstance(value,float):
            value=np.repeat(value,self.n)
        self._a=value
    
    @property
    def b(self):
        return self._b
    @b.setter
    def b(self,value):
        if isinstance(value,int) or isinstance(value,float):
            value=np.repeat(value,self.n+1)
        self._b=value
    
    def _constructTree(self):
        for i in range(self.n+1):
            for j in range(i+1):
                self.tree[i,j]=self.a[i]*np.exp(self.b[j]*j)
    
    @classmethod
    def calibrate(cls,n,q,vol,r,iterations=100):
        '''
        n: number of periods
        q: upward probability
        vol: volatility
        r: spot rate
        '''
        def error(drift):
            rates=BDTrate(n,drift,vol)
            spot_rates=CashPricing(n,q,rates).get_spot_rates()
            error=spot_rates-r
            return error
        initial_guess=np.repeat(.05,n)
        drift=broyden1(error,initial_guess,iter=iterations)
        exp_error=(error(drift)**2).sum()
        return cls(n,drift,vol),exp_error


class PassThroughMBS(object):
    '''
    pass through mortgage backed securitization which 
    consists of only single type of mortgages and a constant prepayment factor in terms of the PSA.
    ---------------
    P: principal payment of the pool
    n: number of periods, will multiply by 12
    loan_r: rate of interest, lending
    pass_r: rate of interest, investors
    PSA: PSA multiplier
    age: age of the pool
    '''
    def __init__(self,P,n,loan_r,pass_r,PSA,age=0):
        self.P=P
        self.n=n*12
        self.loan_r=loan_r/12
        self.pass_r=pass_r/12
        self.PSA=PSA
        self.age=age
        cols=[
            "Total Payment Received",
            "Principal Received",
            "Interest Received",
            "Total Amount Paid",
            "Principal Paid",
            "Interest Paid",
            "Earning",
            "Prepayment Rate",
            "Prepayment Amount",
            "Total OutStanding Amount",
        ]
        data=pd.DataFrame(columns=cols)
        self.data=data
        self._compute_values()

    @property
    def P(self):
        return self._P
    @P.setter
    def P(self,value):
        self._P=value

    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,value):
        self._n=value

    @property
    def loan_r(self):
        return self._loan_r
    @loan_r.setter
    def loan_r(self,value):
        self._loan_r=value

    @property
    def pass_r(self):
        return self._pass_r
    @pass_r.setter
    def pass_r(self,value):
        self._pass_r=value

    @property
    def PSA(self):
        return self._PSA
    @PSA.setter
    def PSA(self,value):
        self._PSA=value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age=value

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,value):
        self._data=value

    def _compute_values(self):
        remainder=self.P
        t=self.age+1
        adjust=self.PSA/100

        while remainder>0:
            pay_rec=remainder*self.loan_r/(1-(1+self.loan_r)**-(self.n-t+1))
            interest_rec=remainder*self.loan_r
            princ_rec=pay_rec-interest_rec
            interest_paid=remainder*self.pass_r
            cpr=adjust*.06*(1 if t > 30 else t/30)
            smm=1-(1-cpr)**(1/12)
            repay_amount=(remainder-princ_rec)*smm
            princ_paid=princ_rec+repay_amount
            tot_paid=princ_paid+interest_paid
            profit=pay_rec-tot_paid
            remainder-=princ_paid
            t+=1

            current_values = {
                "Total Payment Received": pay_rec,
                "Principal Received": princ_rec,
                "Interest Received": interest_rec,
                "Total Amount Paid": tot_paid,
                "Principal Paid": princ_paid,
                "Interest Paid": interest_paid,
                "Earning": profit,
                "Prepayment Rate": smm,
                "Prepayment Amount": repay_amount,
                "Total OutStanding Amount": remainder,
            }

            self.data = self.data.append(current_values,ignore_index=True)
            self.data.index+=1