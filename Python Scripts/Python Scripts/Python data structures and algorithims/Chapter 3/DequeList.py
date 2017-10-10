# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:03:03 2017

@author: Nathan
"""

from UnorderedList import Node

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.numlinks = 0
    
    def __str__(self):
        if self.isEmpty():
            print("Empty Deque")
            return None
        elements = []
        printNode = self.head
        while printNode is not None:
            elements.append(printNode.getData())
            printNode = printNode.getNext()
        print(elements)
    
   
    def addFront(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = self.head
        self.numlinks+=1
    
    def addRear(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.numlinks+=1
        
    def removeFront(self):
        if self.isEmpty():
            print("Empty Deque")
            return None
        
        frontNode = self.head
        self.head = self.head.getNext()
        frontNode.next = None
        if self.head is None:
            self.tail = None
            
        self.numlinks-=1
        return frontNode
    
    def removeRear(self):
        if self.isEmpty():
            print("Deque is Empty")
            return None
        if self.size() == 1:
            tailNode = self.tail
            self.tail = None
            self.head = None
            self.numlinks-=1
            return tailNode
        curr = self.head
        prev = None
        while curr.getNext() is not None:
            prev = curr
            curr = curr.getNext()
        tailNode = curr
        self.tail = prev
        self.tail.next = None
        self.numlinks-=1
        return tailNode
        
    def size(self):
        return self.numlinks
    
    def isEmpty(self):
        return self.numlinks == 0
    
    
d = Deque()
d.addFront(10)
d.addFront(14)
d.addFront(23)
d.__str__()
d.addRear(67)
d.addRear(56)
d.addRear(98)
d.__str__()
d.removeFront()
d.__str__()
d.removeRear()
d.__str__()