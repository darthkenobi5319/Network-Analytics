# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:20:24 2019

@author: Harry
"""
import numpy as np

class adjacencyMatrix:
    def __init__(self):
        fp = open('restaurants.txt')
        record = list()
        for line in fp:
            sline = line.strip()
            snames,restaurant = sline.split(';')
            lnames = snames.split(',')
            record.append(lnames)
        fp.close()
        self.record = record
    
        names = set()
        for i in record:
            for j in i:
                names.add(j)
                
        names = list(names)
        names.sort()
        self.names = names
        length = len(names)
        self.length = length
        countMatrix = np.matrix(np.zeros((length, length)))
        
        
        for i in range(length):
            for j in range(length):
                A = names[i]
                B = names[j]
                if A == B:
                    continue
                else:
                    for k in record:
                        if A in k and B in k:
                            countMatrix[i,j] += 1
                            
        self.matrix = np.triu(countMatrix)
        return
