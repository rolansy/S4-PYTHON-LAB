# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:08:25 2024

@author: ronal
"""

import numpy as np

from scipy.stats import t

n=16
meanmpg=22
sd=3
prempg=20
p=0.05

tobs=(meanmpg-prempg)/(sd/np.sqrt(n))

print("Calculated t value : ",tobs)

df=n-1

t_crit=t.ppf(1-p,df)

print("Table value : ",t_crit)

if tobs>t_crit:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

