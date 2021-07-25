import simple_cal as rk
from Model_Pricing import StockPricing,OptionsPricing,BondPricing,ForwardsPricing,FuturesPricing,SwapsPricing
import numpy as np

#presets
r0=.05
u=1.1
d=0.9
q=.5
n=10
rate_model=StockPricing(n=n,S0=r0,u=u,d=d,c=0)

#ZCB F=100 t=10
F=100
zcb=BondPricing(n=n,F=F,q=q,r=rate_model)
print('1.',end=' ')
print(zcb.price)
#zcb on a forward, t=4
forward=ForwardsPricing(n=4,model=zcb,q=q,r=rate_model)
print('2.',end=' ')
print(forward.price)
#zcb on a future, t=4
future=FuturesPricing(n=4,model=zcb,q=q)
print('3.',end=' ')
print(future.price)
#american call on zcb, t=6, K=80
option=OptionsPricing(n=6,model=zcb,r=rate_model,q=.5,K=80,is_call=True,is_american=True)
print('4.',end=' ')
print(option.price)
#swap,start=2,maturity=11,fixed=.045
swap=SwapsPricing(N=1000000,n=11,q=q,fixed_r=.045,start=2,r=rate_model,is_long=True)
print('5.',end=' ')
print(swap.price)
#compute underlying swap t=5,K=0
option_2=OptionsPricing(n=5,model=swap,r=rate_model,q=.5,K=0,is_call=True,is_american=False)
print('6.',end=' ')
print(option_2.price*1000000)