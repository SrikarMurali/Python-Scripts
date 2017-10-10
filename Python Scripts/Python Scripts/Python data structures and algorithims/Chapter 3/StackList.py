# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 17:15:48 2017

@author: Nathan
"""

from UnorderedList import Node

class Stack:
    
    def __init__(self):
        self.head = None
        self.numlinks = 0
    
    def __str__(self):
        if self.isEmpty():
            print("Empty Stack")
        frontNode = self.head
        while frontNode is not None:
            print(frontNode.getData(), end = " -> ")
            frontNode = frontNode.getNext()
        print("null")
    
    def push(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.numlinks+=1
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        topNode = self.head
        self.head = self.head.getNext()
        topNode.next = None
        self.numlinks-=1
        return topNode
    
    def isEmpty(self):
        return self.numlinks == 0
    
    def size(self):
        return self.numlinks
    
#s = Stack()
#s.push(178)
#s.push(134)
#s.push(656)
#s.push(455)
#s.push(34)
#s.push(23)
#s.pop()
#s.__str__()