# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 02:59:11 2024

@author: ronal
"""

import pandas as pd

d={'State':['Alabama','Alaska','Arizona','Arkanzas','California','Colorado','Connecticut','Delaware'],'Population':[4779736,710231,6392017,2915918,37253956,5029196,3574097,897934],'Murder Rate':[5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8]}

df=pd.DataFrame(d)
df['Murder']=df['Murder Rate']*df['Population']
print(df)
mn=df['Murder'].mean()/100000
print("Mean : ",mn)
print("Median : ",df['Murder'].median()/100000)
tvar=0
for i in range(8):
    tvar+=(df['Murder'][i]-df['Murder'].mean())**2
var=tvar/(8*(100000**2))
print("Variance : ",round(var,2))

