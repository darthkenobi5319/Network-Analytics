# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:37:15 2019

@author: Harry
"""
from adjacencyMatrix import adjacencyMatrix

data = adjacencyMatrix()




x,y = data.matrix.shape

fp = open('problem5.out','w')

for i in range(x):
    name = data.names[i]
    adjacent = list()
    for j in range(y):
        if data.matrix[i,j] >= 1:
            if  data.names[j] not in adjacent:
                adjacent.append(data.names[j])
        if data.matrix[j,i] >= 1:
            if  data.names[j] not in adjacent:
                adjacent.append(data.names[j])
    output = name + ':'
    for k in adjacent:
        output += ' '
        output += k
    print(output,file = fp)
    
fp.close()