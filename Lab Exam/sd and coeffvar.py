# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 07:46:36 2024

@author: ronal
"""

import math as m
import numpy as np
classes=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
freq=[5,10,20,40,30,20,10,5]

mid_classes=[]
for i in classes:
    mid_classes.append((int(i.split('-')[0])+int(i.split('-')[1]))/2)

print(mid_classes)

mean=np.average(mid_classes,weights=freq)
print(mean)

print("median : ",np.median(freq))

variance=np.average((mid_classes-np.average(mid_classes,weights=freq))**2,weights=freq)
print(variance)
sd=m.sqrt(variance)
print("sd : ",sd)
print("Coefficient of var : ",sd/mean)

mean=np.average(mid_classes,weights=freq)
print(mean)
median=np.median(freq)
print(median)

variance=np.average((mid_classes-np.average(mid_classes,weights=freq))**2,weights=freq)
print(variance)
sd=m.sqrt(variance)
print(sd)
print(sd/mean)


variance=np.average((mid_classes-np.average(mid_classes,weights=freq))**2,weights=freq)
print(variance)

mean=np.average(mid_classes,weights=freq)
print(mean)

variance=np.average((mid_classes-mean)**2,weights=freq)
print(variance)