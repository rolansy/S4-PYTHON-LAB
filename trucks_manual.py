import numpy as np
from scipy.stats import t

n=16
mean_per_mpg=22
stand_dev=3
prev_mpg=20
p=0.05

tobs=(mean_per_mpg-prev_mpg)/(stand_dev/np.sqrt(n))
print("Calculated T value : {:.3f}".format(tobs))

df=n-1

t_crit=t.ppf(1-p,df)

print("Table Value: {:.3f}".format(t_crit))

if tobs > t_crit:
    print("Reject Null Hypothesis. Hence the Mileage has improved.")
else:
    print("Accept Null Hypothesis. Hence the Mileage has not improved.")

