import numpy as np
import openpyxl
import scipy.stats
from Model_Pricing import BlackScholes

#presets
wb=openpyxl.load_workbook('EquityDerivsPractice_PSet3.xlsx',read_only=True,data_only=True)['StockPricePaths']
Ts=np.array([[i.value for i in j] for j in wb['A2':'A52']]).flatten()
path1=np.array([[i.value for i in j] for j in wb['B2':'B52']]).flatten()
path2=np.array([[i.value for i in j] for j in wb['C2':'C52']]).flatten()
path3=np.array([[i.value for i in j] for j in wb['D2':'D52']]).flatten()
path4=np.array([[i.value for i in j] for j in wb['E2':'E52']]).flatten()

bs1=BlackScholes(Ts=Ts,t=.25,K=50,path=path1,N=100000,rr=.02)
print('1. ',end=' ')
print(round(bs1.get_annual_vol()*100,2))
print('2. ',end=' ')
print(round(bs1.get_PL_hedge(),0))
bs2=BlackScholes(Ts=Ts,t=.25,K=50,path=path2,N=100000,rr=.02)
print('3. ',end=' ')
print(round(bs2.get_annual_vol()*100,2))
print('4. ',end=' ')
print(round(bs2.get_PL_hedge(),0))
bs3=BlackScholes(Ts=Ts,t=.25,K=50,path=path3,N=100000,rr=.02)
print('5. ',end=' ')
print(round(bs3.get_annual_vol()*100,2))
print('6. ',end=' ')
print(round(bs3.get_PL_hedge(),0))
bs4=BlackScholes(Ts=Ts,t=.25,K=50,path=path4,N=100000,rr=.02)
print('7. ',end=' ')
print(round(bs4.get_annual_vol()*100,2))
print('8. ',end=' ')
print(round(bs4.get_PL_hedge(),0))