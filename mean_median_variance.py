import math as m
import pandas as pd
import numpy as np

d={'State':['Alabama','Alaska','Arizona','Arkanzas','California','Colorado','Connecticut','Delaware'],'Population':[4779736,710231,6392017,2915918,37253956,5029196,3574097,897934],'Murder Rate':[5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8]}
df=pd.DataFrame(d)
df['Murder']=df['Population']*df['Murder Rate']
print(df)
mn=df['Murder'].mean()/100000
print('Mean Murder : ',df['Murder'].mean()/100000)
print('Median Murder : ',df['Murder'].median()/100000)
tvar=0
for i in range(8):
	tvar+=(df['Murder'][i]-df['Murder'].mean())**2
print("Variance Murder : ",tvar/(8*(100000**2)))

