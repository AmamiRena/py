import numpy as np
import simple_cal as rk
from Model_Pricing import CAPM,VaR
import scipy.stats

mu=np.array([-0.5186,4.7057,-0.6986])/100
mu_=np.array([6,2,4])/100
V=np.array([[0.0056,-0.0020,0.0037],
            [-0.0020,0.0022,-0.0022],
            [0.0037,-0.0022,0.0074]])
rr=.01

portfolio=CAPM(r=mu,r_=mu_,cov=V)
ret=portfolio.max_cml(rr=.01,sigma=.05)
print('1.',end=' ')
print(round(ret*100,2))
exp_ret=portfolio.max_cml(rr=.01,sigma=.05,is_realized=True)
print('2.',end=' ')
print(round(exp_ret*100,2))
loss_list=VaR(np.array([-1.1168,-1.3565,1.3754,-1.0396,0.5662,-0.0050,-1.9092,1.1039,-0.2332,-0.6678,-1.3045,
                        0.8229,0.9616,-0.9685,1.0631,-2.8888,0.6022,1.1204,-0.9511,0.0810,-0.8619,0.0685,-0.2053,
                        0.9565,0.1795,-2.4565,-0.0656,-0.1942,0.3471,-0.2564,1.2923,-0.3045,0.4619,-1.8819,-1.1397,1.9877,
                        -0.0960,1.0440,-0.2722,-0.0218,0.8140,1.9191,2.1450,-0.3924,0.8846,-2.0569,-0.8699,-0.4551,-0.5114,
                        -0.0412,0.2515,-0.6077,1.8807,-0.2756,-1.2639,-1.4916,-0.9395,2.3707,-0.2759,-0.7360])*-1.0)
var=loss_list.get_VaR()
print('3.',end=' ')
print(round(var,2))
cvar=loss_list.get_VaR(is_conditional=True)
print('4.',end=' ')
print(round(cvar,2))
print('5.',end=' ')
print(round(1-scipy.stats.binom.cdf(11,15,.5),4))
print('6.',end=' ')
print(round(1-(scipy.stats.binom.cdf(13,15,0.5))**100,4))