# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:37:09 2024

@author: ronal
"""

import pandas as pd

from scipy.stats import chi2_contingency as c2

data={'High school':[60,40,100],'Bachelors':[54,44,98],'Masters':[46,53,99],'PHD':[41,57,98],'Total':[201,194,395]}

index=['Female','Male','Total']

df=pd.DataFrame(data,index)
print(df)

ct=[df.loc['Female'],df.loc['Male']]

print(ct)

chi2s,pv,dof,expected=c2(ct)

print("ch2 statistic : ",chi2s)
print("p value : ",pv)
print("dof : ",dof)
print("Expected  : ",expected)

df2=pd.DataFrame(expected,index=index[:-1],columns=list(data.keys()))

print(df2)

if pv<0.05:
    print("Reject Null Hypothesis. dependant and significant")
else:
    print("Fail to Reject Null Hypothesis. independant and insignificant " )