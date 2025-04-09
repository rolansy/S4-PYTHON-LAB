# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 04:00:26 2024

@author: ronal
"""

import pandas as pd
from scipy.stats import chi2_contingency as c2

d={'High School':[60,40,100],
   'Bach':[54,44,98],
   'Masters':[46,53,99],
   'PHD':[41,57,98],
   'Total':[201,194,395]}


index=['Fem','Male','Total']
df=pd.DataFrame(d,index)
print(df)
ct=[df.loc['Fem'],df.loc['Male']]

chi2,p,dof,expected=c2(ct)

print("Chi squared : ",chi2)
print("p value : ",p)
print("DOF : ",dof)
print("Expected : ")

df2=pd.DataFrame(expected,columns=d.keys(),index=index[:2])
print(df2)

if p<0.05:
    print("Reject NUll, they are dependent")
else:
    print("Acept null hypo, they independent")