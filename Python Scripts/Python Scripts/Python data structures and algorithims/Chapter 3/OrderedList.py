# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:28:49 2017

@author: Nathan
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
        
class OrderedList:
    def __init__(self):
        self.head = None
        self.numlinks = 0
    
    def __str__(self):
        if self.isEmpty():
            print("Empty List")
            return None
        
        element = []
        curr = self.head
        while curr.getNext() is not None:
            element.append(curr.getData())
            curr = curr.getNext()
        print(element)
    
    def index(self, item):
        idx = 0
        curr = self.head
        found = False
        while curr is not None:
            if curr.getData() == item:
                found = True
                break
            else:
                curr = curr.getNext()
                idx+=1
        if not found:
            return None
        return idx
    
    def getItem(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.getNext()
        
        if curr != None:
            return curr.getData()
        else:
            raise("Invalid Index")
            
    def pop(self, index):
        return self.remove(self.getItem(index))
    
    def insert(self, index, item):
        
        curr = self.head
        for i in range(index):
            curr = curr.getNext()
        
        if curr is not None:
            newNode = Node(item)
            newNode.setNext(curr.getNext())
            curr.setNext(newNode)
        else:
            raise("Invalid Index")
        
        
        
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        curr = self.head
        prev = None
        stop = False
        while curr != None and not stop:
            if curr.getData() > item:
                stop = True
            else:
                prev = curr
                curr = curr.getNext()
        
        temp = Node(item)
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(curr)
            prev.setNext(temp)
        self.numlinks+=1
        
    def length(self):
        return self.numlinks
    
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:
            if current.getNext == None:
                prev.setNext(None)
            else:
                prev.setNext(current.getNext())
        self.numlinks-=1


o = OrderedList()
o.add(14)
o.add(23)
o.add(25)
o.add(656)
o.insert(1, 43)
o.insert(3, 34)
o.__str__()
o.pop(0)
o.__str__()
