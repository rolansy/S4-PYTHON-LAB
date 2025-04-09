# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:51:30 2024

@author: ronal
"""

import numpy as np
import pandas as pd
import math as map
d={'State':['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware'],'Population':[4779736,710231,6392017,2915918,37253956,5029196,3574097,897934],'Murder Rate':[5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8]}

df=pd.DataFrame(d)

df['Murder']=df['Population']*df["Murder Rate"]/100000

print(df)

mn=df['Murder'].mean()
print("mean : ",mn)
md=df['Murder'].median()
print('Meidan : {:4.3f}'.format(mn))
var=df['Murder'].var()
'''
tvar=0
for i in range(len(df['State'])):
    tvar+=
'''
tvar=0
for i in range(len(df["State"])):
    tvar+=((df['Murder'][i]-df['Murder'].mean())**2)
    
tvar=0
for i in range(len(df['State'])):
    tvar+=(df['Murder'][i]-df['Murder'].mean())**2
print("Variance : ",round(tvar/8,4))

mn=df['Murder'].mean()

tvar=0
for i in range(len(df['Murder'])):
    tvar+=(df['Murder'][i]-mn)**2
print("Varicane : ",tvar/8)

