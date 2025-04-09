# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:24:42 2024

@author: ronal
"""

import matplotlib.pyplot as plt

countries=['Africe','North Am','Asia','Oceania','Europa','South Am','Soviet Un']
areas=[11.7,9.4,10.4,3.3,1.9,6.9,7.9]

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # blue, green, red, cyan, magenta, yellow, black

plt.bar(countries,areas,color=colors)
plt.xlabel('countries')
plt.ylabel('areas')
plt.show()