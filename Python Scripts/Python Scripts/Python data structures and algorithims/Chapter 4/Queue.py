# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:37:56 2017

@author: Nathan
"""
import random

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
def hotpotato(names, num):
    simqueue = Queue()
    size = len(names)
    for name in names:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1:
        r = random.randint(size, size**2)
        for i in range(r):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotpotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))