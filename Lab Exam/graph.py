# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:01:36 2024

@author: ronal
"""

import matplotlib.pyplot as plt
import numpy as np
import math as m



plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid=True
plt.legend()
ch=0

while (ch!=10):
    print("\n1.y=x\n2.y=x^2\n3.y=2^x\n4.y=sinx\n5.y=cosx\n6.y=e^x\n10.exit\n")
    ch=int(input("Enter CJoice  : "))
    plt.style.use('seaborn-v0_8-pastel')
    if ch==1:
        x=np.linspace(-10, 10,100)
        y=x
        plt.title("Graph of y=x")
        plt.plot(x, y, linewidth=2, marker='^', markersize=5, label='y=x',color='violet')

        plt.show()
    elif ch==2:
        x=np.linspace(-10, 10,100)
        y=x**2
        plt.title("Graph of y=x^2")
        plt.plot(x, y, linewidth=2, marker='^', markersize=5, label='y=x^2',color='blue')
        plt.show()
    elif ch==3:
        x=np.linspace(-10, 10,100)
        y=[2**i for i in x]
        plt.title("Graph of y=2^x")
        plt.plot(x, y, linewidth=2, marker='^', markersize=5, label='y=2^x',color='blue')
        plt.show()
    elif ch==4:
        x=np.linspace(-10, 10,100)
        y=[m.sin(i) for i in x]
        plt.title("Graph of y=sin(x)")
        plt.plot(x, y, linewidth=2, marker='^', markersize=5, label='y=2^x',color='blue')
        plt.show()
    elif ch==5:
        x=np.linspace(-10, 10,100)
        y=[m.cos(i) for i in x]
        plt.title("Graph of y=cos(x)")
        plt.plot(x, y, linewidth=2, marker='^', markersize=5, label='y=2^x',color='blue')
        plt.show()
    elif ch==6:
        x=np.linspace(-10,10,500)
        y=[m.exp(i) for i in x]
        plt.plot(x,y,marker='^',markersize=5)
        plt.show()
        