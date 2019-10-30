# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:37:15 2019

@author: Harry
"""
fp = open('problem2.out')
record1 = 0




for line in fp:
    record1 += 1
    

fp.close()

fp = open('problem4.out')
record2 = 0




for line in fp:
    sline = line.strip()
    name,degree = sline.split(' ')
    record2 += int(degree)
    
fp.close()

fp = open('question1.txt','w')
print(2,file = fp)
print(record1,file = fp)
print(record2,file = fp)
fp.close()