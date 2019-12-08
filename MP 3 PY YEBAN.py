# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:27:33 2019

@author: ASUS
"""
import numpy as py

array=eval(input('Enter data (sample[[x],[y]]) \n'))
y1=py.array([array[1]])    #axis 1 of created array
x1=py.array([array[0]])      #axis 2
x1=x1.flatten()
y1=y1.flatten()
if len(x1)>=11:
    M=10
else:
    M=len(x1)-1
n=py.zeros((M,1))
for i in range (1,M):
    p=py.polyfit(x1,y1,i)
    o=py.polyval(p,x1)
    g=(y1-o)
    n[i-1,0]=py.linalg.norm(g)
    I=n.argmin()
    I1=I+1
    coefficients=py.polyfit(x1,y1,I1)
    print('The coefficients are: \n',coefficients)