# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 04:22:00 2024

@author: ronal
"""

import pandas as pd
tb={'Person':['A','B','C','D','E'],'hand':[17,15,19,17,21],'height':[150,154,169,172,175]}

df=pd.DataFrame(tb)

corr = df[['hand', 'height']]
correlation_coefficient = corr.corr().iloc[0,1]
print(correlation_coefficient)

