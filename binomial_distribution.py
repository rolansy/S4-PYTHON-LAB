import numpy as np

n=6
p=0.25

def binomial(k):
    nck=np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))
    return nck*(p**k)*((1-p)**(n-k))

print("4 Successes:",binomial(4))
success=binomial(0)
success=1-success
print("Atleast 1 Success:",success)
