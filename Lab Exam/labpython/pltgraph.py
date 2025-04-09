# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 00:07:19 2024

@author: ronal
"""

import matplotlib.pyplot as plt
import math as m
import numpy as np


def f1():
    plt.title("linear")
    plt.xticks(list(range(-10,10,5)))
    plt.xlim(-10,5)
    plt.legend()
    x=np.linspace(-15,10,500)
    y=[i for i in x]
    plt.plot(x,y)
    plt.show()

def f2():
    x=np.linspace(-10,10,500)
    y=[i**2 for i in x]
    plt.plot(x,y)
    plt.show()
    
def f3():
    x=np.linspace(-10,10,500)
    y=[2**i for i in x]
    plt.plot(x,y)
    plt.show()
    
def f4():
    x=np.linspace(-10,10,500)
    y=[m.sin(i) for i in x]
    plt.plot(x,y)
    plt.show()

def f5():
    x=np.linspace(-10,10,500)
    y=[m.cos(i) for i in x]
    plt.plot(x,y)
    plt.show()

def f6():
    x=np.linspace(-10,10,500)
    y=[m.exp(i) for i in x]
    plt.title("Expo")
    plt.plot(x,y)
    plt.show()


while True:
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True)
    print("\n1.y=x\n2.y=x^2\n3.y=2^x\n4.y=sinx\n5.y=cos\n6.y=e^x\n7.exit")
    c=int(input("Enter CHoiceL  :  "))
    if c==7:
        break
    elif c==1:
        f1()
    elif c==2:
        f2()
    elif c==3:
        f3()
    elif c==4:
        f4()
    elif c==5:
        f5()
    elif c==6:
        f6()
        
    