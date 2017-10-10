# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:32:18 2017

@author: Nathan
"""

class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

def palchecker(word):
    chardeque = Deque()
    
    for char in word:
        chardeque.addRear(char)
    
    
    while chardeque.size() > 1:
        first = chardeque.removeFront()
        second = chardeque.removeRear()
        if first != second:
            return False
    return True


print(palchecker("lsd"))
print(palchecker("racecar"))
    