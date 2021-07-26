import pandas as pd
import numpy as np
import simple_cal as rk
from Model_Pricing import CAPM

#presets
mu=np.array([6,2,4])/100
v=np.array([[8,-2,4],
            [-2,2,-2],
            [4,-2,8]])*10**-3
rr=.01

portfolio=CAPM(r=mu,cov=v)
portfolio.plot_eff_frontier(n_points=25,show_cml=True,rr=0,show_ew=True,show_gmv=True)

#equally-weighted 1,1,1
weights=np.array([1,1,1])/3
ret,vol=portfolio.get_rv(weights)
print('1.',end=' ')
print(round(ret*100,2))
#
print('2.',end=' ')
print(round(vol*100,2))
#gmv,return
weights_gmv=portfolio.gmv()
ret,vol=portfolio.get_rv(weights_gmv)
print('3.',end=' ')
print(round(ret*100,2))
#max sharpe,return
weights_msr=portfolio.max_sharpe_ratio(rr=rr)
ret,vol=portfolio.get_rv(weights_msr)
print('4.',end=' ')
print(round(ret*100,2))
#vol
print('5.',end=' ')
print(round(vol*100,2))
#slope of cml
slope,intercept=portfolio.get_cml(rr=rr)
print('6.',end=' ')
print(round(slope,2))
#sigma=.05, max return
ret=portfolio.max_cml(rr=rr)
print('7.',end=' ')
print(round(ret*100,2))