import matplotlib.pyplot as plt
import numpy as np

classs=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
freq=[5,10,20,40,30,20,10,5]

mid_class=[]
for i in range(len(classs)):
    mid_class.append((int(classs[i].split('-')[0])+int(classs[i].split('-')[1]))/2)
print(mid_class)
print(freq)

print("Mean : ",np.average(mid_class, weights=freq))
print("Median : ",np.median(freq))
print("Variance : ",np.var(freq))
print("Standard Deviation : ",np.std(freq))
print("Coefficient of Variation : ",(np.std(freq)/np.mean(freq))*100)


