# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:44:09 2024

@author: ronal
"""

import matplotlib.pyplot as plt
import numpy as np

edges=[135,140,145,150,155]
heights=[4,12,16,8]
cs='magenta'
plt.hist(edges[:-1],bins=edges,weights=heights,edgecolor='cyan',color=cs)
plt.yticks(np.arange(0,20,0.5))
plt.show()