# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 03:26:24 2024

@author: ronal
"""
from numpy import math as m


n=6
p=0.25

def binomial(k):
    nck=m.factorial(n)/(m.factorial(k)*m.factorial(n-k))
    return nck*(p**k)*((1-p)**(n-k))

print("4 sucess : ",binomial(4))

print("at least 1 : ",1-binomial(0))
