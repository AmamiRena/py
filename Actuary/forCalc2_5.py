import numpy as np
import openpyxl
from Model_Pricing import CDO

#presets
wb=openpyxl.load_workbook('StructuredCredit_PSet4.xlsx',read_only=True,data_only=True)['LossDistributionCalculations']
probs=np.array([[i.value for i in j] for j in wb['C3':'C22']]).flatten()

credit_default=CDO(probs)
print('1. ',end='')
print(credit_default.get_pn(3))
print('2. ',end='')
print(credit_default.exp_loss())
print('3. ',end='')
print(credit_default.exp_loss_var())
print('4. ',end='')
print(credit_default.exp_tranche_loss(0,2))
print('5. ',end='')
print(credit_default.exp_tranche_loss(2,4))
print('6. ',end='')
print(credit_default.exp_tranche_loss(4,20))