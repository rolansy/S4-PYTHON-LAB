import random as rd
import numpy as np
from scipy import stats as st

mean_per_mpg=22
stand_dev=3
prev_mpg=20
prob=0.05

mpg=np.random.normal(mean_per_mpg,stand_dev,16)

print(mpg) 

t_stat,p_vak=st.ttest_1samp(mpg,prev_mpg)

print("T-Statistics : ",t_stat)
print("P-Value : ",p_vak)

if p_vak < prob:
    print("Reject Null Hypothesis.")
else:
    print("Accept Null Hypothesis.")

