# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:56:12 2017

@author: Nathan
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)