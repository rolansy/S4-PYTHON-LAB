# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:03:30 2024

@author: ronal
"""

import pandas as pd

tb={'Person':['A','B','C','D','E'],'hand':[17,15,19,17,21],'height':[150,154,169,172,175]}

df=pd.DataFrame(tb)
print(df)

corr=df[['hand','height']].corr()

print(corr)

print(corr.loc['hand']['height'])