# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:02:56 2024

@author: ronal
"""

f=open("file.txt",r)
s=f.readlines(f)
print("Number of sentences : ",len(s))
wc=cc=uc=lc=sc=0
cc=0
for i in s:
    sl=i.split(" ")
    for x in sl:
        cc+=1
        if not x.isnumeric():
            wc+=1
        for j in x:
            if j.isupper():
                uc+=1
            elif j.islower():
                lc+=1
            elif not j.isalnum():
                sc+=1