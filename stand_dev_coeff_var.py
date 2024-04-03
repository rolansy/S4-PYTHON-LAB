import math as m
import numpy as np

classs=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
freq=[5,10,20,40,30,20,10,5]

mid_class=[]
for i in range(len(classs)):
    mid_class.append((int(classs[i].split('-')[0])+int(classs[i].split('-')[1]))/2)
print(mid_class)
print(freq)

mean=np.average(mid_class, weights=freq)
print("Mean : ",mean)
print("Median : ",np.median(freq))
variance = np.average((mid_class - np.average(mid_class, weights=freq))**2, weights=freq)
print("Variance : ", variance)
sd=m.sqrt(variance)
print("Standard Deviation : ",sd)
print("Coefficient of Variation : ",(sd/mean))


