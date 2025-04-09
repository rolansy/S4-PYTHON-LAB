# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:56:31 2024

@author: ronal
"""

import matplotlib.pyplot as plt
import numpy as np
import math as m
plt.yticks(np.arange(-1,11,0.5))
plt.grid(True)

colors=['b','yellow','cyan','magenta','g','r']

x=np.linspace(-10,10,500)

for i in range(6):
    y=[m.sin(z) for z in x]
    
    mx=[j+((i+1)*m.pi)/3 for j in x]
    plt.plot(mx,y,color=colors[i])
plt.xlim(0,10)
plt.title('6 sin x')
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
