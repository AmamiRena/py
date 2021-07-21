from abc import ABC
from collections import Iterable
import numpy as np

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

#Basic Pricing always go through
class StockPricing(BinomialTree):
    '''
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


class OptionsPricing(BinomialTree):
    '''
    n: number of periods
    model: tree
    r: interet
    q: upward probability
    K: strike price
    is_call: True if call option, False for put option
    is_american: True if american option, False for EU option
    '''
    __doc__+=BinomialTree.__doc__

    def __init__(self,n,model,r,q,K,is_call=True,is_american=False):
        '''
        Black Scholes Model
        '''
        super().__init__(n,q)
        self.K=K
        self.adjuster=1 if is_call else -1
        self.is_american=is_american
        self._early_exercise=[]
        self._constructTree(model,r)

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
        return self.tree[0,0]
    
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
    r: interest
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