# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 03:09:41 2024

@author: ronal
"""
import numpy as np
import math as m

classes=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
freq=[5,10,20,40,30,20,10,5]
mid_classes=[]
for i in range(len(classes)):
    mid_classes.append((int(classes[i].split('-')[0])+int(classes[i].split('-')[1]))/2)
print(mid_classes)
mean=np.average(mid_classes,weights=freq)
print("MEan : ",mean)
print("Mean : ",np.average(mid_classes,weights=freq))
variance=np.average((mid_classes-np.average(mid_classes,weights=freq))**2,weights=freq)
print("Variance : ",variance)
print("Variance : ",np.average((mid_classes-np.average(mid_classes,weights=freq))**2,weights=freq))
print("Standard dev : ",m.sqrt(variance))
print("Coeff of var : ",m.sqrt(variance)/mean)



