# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:08:20 2024

@author: ronal
"""

import numpy as np
n=6
p=0.25

def binomial(k):
    nck=np.math.factorial(n)/(np.math.factorial(n-k)*np.math.factorial(k))
    return nck*(p**k)*((1-p)**(n-k))

print(" 4 success Bnomial : ",binomial(4))
success1=1-binomial(0)
print("1 success : ",success1)