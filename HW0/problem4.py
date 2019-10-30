# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:37:15 2019

@author: Harry
"""
from adjacencyMatrix import adjacencyMatrix

data = adjacencyMatrix()




x,y = data.matrix.shape

fp = open('problem4.out','w')

for i in range(x):
    count = 0
    for j in range(y):
        if data.matrix[i,j] >= 1:
            count += 1
        if data.matrix[j,i] >= 1:
            count += 1
    print(data.names[i],count,sep=' ',file = fp)
    
fp.close()