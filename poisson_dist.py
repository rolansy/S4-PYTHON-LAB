import numpy as np
import math as m

mean=3.4
k=6
def poisson(mean,k):
    return ((mean**k)*m.exp(-mean))/m.factorial(k)
print("Probability : ",poisson(mean,k))
