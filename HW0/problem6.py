# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:59:53 2019

@author: Harry
"""
import numpy as np

fp = open('problem5.out')
record = dict()
for line in fp:
    sline = line.strip()
    name,sfriends = sline.split(':')
    friends = sfriends[1:].split(' ')
    record[name] = friends
fp.close()


class node:
    def __init__(self,name):
        self.visited = False
        self.name = name
        self.distance = 0
        
from adjacencyMatrix import adjacencyMatrix
data = adjacencyMatrix()


listNode = list()
for i in data.names:
    i = node(i)
    listNode.append(i)



    
def initialize(name):
    i = data.names.index(name)
    listNode[i].visited = True
    queue = [listNode[i]]
    return queue

def dequeue(queue,n):
    if queue == []:
        return
    else:
        distance = n.distance + 1
        name = n.name
        queue.remove(n)
        for i in record[name]:
            index = data.names.index(i)
            if listNode[index].visited == False:
                listNode[index].visited = True
                listNode[index].distance = distance
                queue.append(listNode[index])
        if queue == []:
            return
        else:
            new = queue[0]
            return dequeue(queue,new)
        
        
def calcDistance(root):
    global listNode
    queue = initialize(root)
    n = listNode[data.names.index(root)]
    dequeue(queue,n)
    result = dict()
    for i in range(len(listNode)):
        #print(data.names[i],listNode[i].distance,sep = ' ')
        result[data.names[i]] = listNode[i].distance 
    listNode = list()
    for i in data.names:
        i = node(i)
        listNode.append(i)
    return result

    
def calcAverage(root):
    result = calcDistance(root)
    distances = list()
    for i in result.keys():
        distances.append(result[i])
    avg = np.average(np.array(distances))
    return avg


fp = open('problem6.out','w')
for i in data.names:
    print(i,calcAverage(i),sep = ' ',file = fp)
    
fp.close()
    