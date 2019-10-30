# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:00:24 2019

@author: Harry
"""

fp = open('restaurants.txt')
record = dict()

def recAdd(restaurant,names):
    if restaurant not in record.keys():
        record[restaurant] = set(names)
    else:
        for i in names:
            record[restaurant].add(i)
    return


for line in fp:
    sline = line.strip()
    snames,restaurant = sline.split(';')
    lnames = snames.split(',')
    recAdd(restaurant,lnames)
fp.close()
    
fp = open('problem1.out','w')

for i in record.keys():
    newline = i +': '
    for j in record[i]:
        newline += (j + ' ')
    line = newline.strip()
    print(line,file = fp)

print(record)    
 