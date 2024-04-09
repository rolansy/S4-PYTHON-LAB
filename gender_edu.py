import pandas as pd
from scipy.stats import chi2_contingency as c2

data={
    'High School':[60,40,100],
    'Bachelors':[54,44,98],
    'Masters':[46,53,99],
    'Ph.d.':[41,57,98],
    'Total':[201,194,395]
    
}

index=['Female','Male','Total']
df=pd.DataFrame(data,index)
print(df)
ct=[df.loc['Female'],df.loc['Male']]

#print(df.loc['Female'])
#print(list(df.loc['Female']))

chi2,p,dof,expected=c2(ct)
print("Chi-square : ",chi2)
print("Table Value : ",7.815)
print("Degree of Freedom : ",dof)
print("P-Value : ",p)
print("Expected : ")

df2=pd.DataFrame(expected,columns=['High School','Bachelors','Masters','Ph.d.','Total'],index=['Female','Male'])
print(df2)



if p < 0.05:
    print("Gender and Education Level are dependent.")
else:
    print("Gender and Education Level are independent.")
