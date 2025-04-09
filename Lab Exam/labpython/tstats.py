# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 04:25:27 2024

@author: ronal
"""

import numpy as np
from scipy.stats import t
import math as m

n=16
mean_per_mpg=22
sd=3
prevmpg=20
p=0.05
quit()
tobs=(mean_per_mpg-prevmpg)/(sd/m.sqrt(n))
print("Calculated T Value  : ",tobs)

df=n-1
t_crit=t.ppf(1-p,df)
print(t_crit)

if tobs>t_crit:
    print("Reject NUll Hypothesis ,mileage improved")
else:
    print("Mileage not improve")


