# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:31:15 2024

@author: ronal
"""
import math as m
import numpy as np

mean=3.4
k=6

def poisson(mean,k):
    return (((mean)**k)*m.exp(-mean))/np.math.factorial(k)

print("P x=6 : ",poisson(mean, k))