# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:59:53 2019

@author: Harry
"""
fp = open('problem5.out')
record = dict()
for line in fp:
    sline = line.strip()
    name,sfriends = sline.split(':')
    friends = sfriends.split(' ')
    record[name] = friends
fp.close()

from adjacencyMatrix import adjacencyMatrix
data = adjacencyMatrix()

class node:
    def __init__(self,name):
        self.visited = False
        self.name = name
        self.distance = 0

listNode = list()
for i in data.names:
    i = node(i)
    listNode.append(i)
    


#def dequeue(queue,n):