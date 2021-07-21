import simple_cal as rk
from Model_Pricing import StockPricing,FuturesPricing,OptionsPricing
import numpy as np

#default
params=rk.blackscholes_to_binomial(.02,.3,15,.25,.01)
u=params['upward_drift']
d=params['downward_drift']
div=params['dividend_per_period']
r=params['risk_free_rate']
model=StockPricing(n=15,S0=100,u=u,d=d,c=div)
q=((1+r)-d-div)/(u-d)

#American Call, K=110, T=.25
call_option=OptionsPricing(n=15,model=model,r=r,q=q,K=110,is_call=True,is_american=True)
print('1. ',end='')
print(call_option.price)
#American put
put_option=OptionsPricing(n=15,model=model,r=r,q=q,K=110,is_call=False,is_american=True)
print('2. ',end='')
print(put_option.price)
#if early exercise
print('3. ',end='')
print(True if put_option.early_exercise else False)
#earliest exercise
print('4. ',end='')
print(put_option.early_exercise[0])
#american call K=110,n=10 on a futures n=15 periods
model1=FuturesPricing(n=15,model=model,q=q)
call_on_futures=OptionsPricing(n=10,model=model1,r=r,q=q,K=110,is_call=True,is_american=True)
print('6. ',end='')
print(call_on_futures.price)
#earliest exercise
print('7. ',end='')
print(call_on_futures.early_exercise[0]['Time'])
#chooser c/p, period=10,K=100, option period=5
p=10
tree=np.zeros([p+1,p+1])
call_option=OptionsPricing(n=15,model=model,r=r,q=q,K=100,is_call=True,is_american=False)
put_option=OptionsPricing(n=15,model=model,r=r,q=q,K=100,is_call=False,is_american=False)
for i in range(p,-1,-1):
    if i==p:
        for j in range(i+1):
            tree[i,j]=max(call_option.tree[i,j],put_option.tree[i,j])
    else:
        for j in range(i+1):
            cd=tree[i+1,j]
            cu=tree[i+1,j+1]
            price=(q*cu+(1-q)*cd)/(1+r)
            tree[i,j]=price
print('8. ',end='')
print(tree[0,0])