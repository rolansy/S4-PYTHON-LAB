# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 03:52:52 2024

@author: ronal
"""

import math as m

mn=3.4
x=6
def poisson(k):
    return( (m.exp(-mn) * (mn**k))/m.factorial(k))

print("Probability : ",poisson(x))

            