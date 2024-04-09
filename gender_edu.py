import pandas as pd
from scipy.stats import chi2_contingency as c2

tb={
    'edu':['High School','Bachelors','Masters','Ph.d.','Total'],
    'Female':[60,54,46,41,201],
    'Male':[40,44,53,57,194],
    'Total':[100,98,99,98,395]
    
}

df=pd.DataFrame(tb)
print(df)
contingency_table=pd.crosstab(df['Total'],df['edu'])
print(contingency_table)

chi2,p,dof,excepted=c2(contingency_table.values)
print("Chi-square Statistics : ",chi2)
print("Degree of Freedom : ",dof)
print("P-Value : ",p)

if p < 0.05:
    print("Gender and Education Level are dependent.")
else:
    print("Gender and Education Level are independent.")