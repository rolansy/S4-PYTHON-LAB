# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 00:02:51 2024

@author: ronal
"""

f1=open("file.txt",'r')
f2=open("copy.txt",'w')

for line in f1.readlines():
    for i in line:
        if i.isalnum() or i=="\n" or i==" " or i=="\t" or i=="":
            f2.write(i)
f1.close()
f2.close()
    