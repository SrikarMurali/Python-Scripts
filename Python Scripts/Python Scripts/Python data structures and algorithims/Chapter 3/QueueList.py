# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:41:38 2017

@author: Nathan
"""

from UnorderedList import Node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.numlinks = 0
    
    def enqueue(self, data):
        newNode = Node(data)
        
        if self.front is None:
            self.front = newNode
            self.back = self.front
        else:
            self.back.setNext(newNode)
            self.back = self.back.getNext()
        self.numlinks+=1
    
    def dequeue(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        frontNode = self.front
        if self.front.getNext() is None:
            self.front = None
            self.back = None
        else:
            self.front = self.front.getNext()
        self.numlinks-=1
        return frontNode
    
    def qprint(self):
        if not self.isEmpty():
            frontNode = self.front
            while not frontNode is None:
                print(frontNode.getData(), end = " -> ")
                frontNode = frontNode.getNext()
            print("null")
        else:
            print("Empty Queue")
            
    def isEmpty(self):
        return self.numlinks == 0
    
    def size(self):
        return self.numlinks
    
q = Queue()

q.enqueue(17)
q.enqueue(12)
q.enqueue(15)
q.enqueue(23)
q.enqueue(243)
q.enqueue(1433)
q.qprint()
q.dequeue()
q.qprint()