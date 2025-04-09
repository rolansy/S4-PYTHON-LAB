# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 01:26:07 2024

@author: ronal
"""

import matplotlib.pyplot as plt

edges=list(range(135,156,5))
heights=[4,12,16,8]
print(edges[:-1])
plt.hist(edges[:-1],bins=edges,weights=heights,edgecolor='black',color='r')
plt.xticks(range(135,156,5))
plt.show()