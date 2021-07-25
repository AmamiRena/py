import numpy as np
import simple_cal as rk
from Model_Pricing import BDTrate,OptionsPricing,StockPricing,SwapsPricing,BondPricing

#presets
n=10
r=np.array([3,3.1,3.2,3.3,3.4,3.5,3.55,3.6,3.65,3.7])/100
q=.5

#b=0.05 for BDT, after calibration, t=3 swaption with 1m,start=4,K=0,r=.039
rates,error=BDTrate.calibrate(n=n,q=q,vol=.05,r=r)
swap=SwapsPricing(N=1000000,n=n,q=q,fixed_r=.039,start=4,r=rates,is_long=True)
option=OptionsPricing(N=1000000,n=3,model=swap,r=rates,q=q,K=0,is_call=True,is_american=False)
print('1.',end=' ')
print(error)
print(option.price)
#b=0.1
rates,error=BDTrate.calibrate(n=n,q=q,vol=.1,r=r)
swap=SwapsPricing(N=1000000,n=n,q=q,fixed_r=.039,start=4,r=rates,is_long=True)
option=OptionsPricing(N=1000000,n=3,model=swap,r=rates,q=q,K=0,is_call=True,is_american=False)
print('2.',end=' ')
print(error)
print(option.price)
#binomial model,n=10,r0=.05,u=1.1,d=.9,q=.5; hazard a=.01,b=1.01.R=.2,F=100
rate_model=StockPricing(n=10,S0=.05,u=1.1,d=.9)
hazard={'a':.01,'b':1.01,'recovery_rate':.2}
bond=BondPricing(n=10,F=100,q=.5,r=rate_model,hazard=hazard)
print('3.',end=' ')
print(bond.price)