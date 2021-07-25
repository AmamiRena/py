import numpy as np
import simple_cal as rk
from Model_Pricing import Annuity,PassThroughMBS

#monthly,principal, 30 year, r=.05, p=400000
mortgage=Annuity(p=400000,r=.05,t=30,is_principal=True,is_monthly=True)
print('1.',end=' ')
print(mortgage.monthly_payment)
#P=400m,n=20,loan=.06,pass_through=.05,psa=100
mortgage_pool=PassThroughMBS(P=400,n=20,loan_r=.06,pass_r=.05,PSA=100)
#print('*'*40)
#print(mortgage_pool.data.head())
#print('*'*40)
#interest paid
print('2.',end=' ')
print(mortgage_pool.data['Interest Paid'].sum())
#total prepayments
print('3.',end=' ')
print(mortgage_pool.data['Prepayment Amount'].sum())
#psa=200,total prepayments
print('4.',end=' ')
mortgage_pool=PassThroughMBS(P=400,n=20,loan_r=.06,pass_r=.05,PSA=200)
print(mortgage_pool.data['Prepayment Amount'].sum())
#pv of PO MBS r=.045
mortgage_pool=PassThroughMBS(P=400,n=20,loan_r=.06,pass_r=.05,PSA=100)
pv=rk.present_value(mortgage_pool.data['Principal Paid'],.045/12)
print('5.',end=' ')
print(pv)
#IO MBS
pv_r=rk.present_value(mortgage_pool.data['Interest Paid'],.045/12)
print('6.',end=' ')
print(pv_r)
#duration IO MBS
print('7.',end=' ')
print(rk.duration(mortgage_pool.data['Interest Paid'])/12)
#r=.045 --> .035, loss/gain?
pv_nr=rk.present_value(mortgage_pool.data['Interest Paid'],.035/12)
print('8.',end=' ')
print(pv_nr-pv_r)
#r=.045 --> .035, psa=100 --> 150
mortgage_pool=PassThroughMBS(P=400,n=20,loan_r=.06,pass_r=.05,PSA=150)
pv_3=rk.present_value(mortgage_pool.data['Interest Paid'],.035/12)
print('9.',end=' ')
print(pv_3-pv_r)