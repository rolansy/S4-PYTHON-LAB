import matplotlib.pyplot as plt
import pandas as pd

d={'State':['Alabama','Alaska','Arizona','Arkanzas','California','Colorado','Connecticut','Delaware'],'Population':[4779736,710231,6392017,2915918,37253956,5029196,3574097,897934],'Murder Rate':[5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8]}
df=pd.DataFrame(d)
print(df)
print('Mean Population : ',df['Population'].mean())
print('Mean Murder (per 100k per year) : ',df['Murder Rate'].mean())

