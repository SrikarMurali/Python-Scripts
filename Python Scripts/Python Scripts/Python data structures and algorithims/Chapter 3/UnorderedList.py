# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:52:19 2017

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

class UnorderedList:
    def __init__(self):
        self.head = None
        self.numlinks = 0
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.numlinks+=1
        
    def length(self):
        return self.numlinks
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
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
    
    def remove(self, item):
        if not self.search(item):
            print("Item not in list")
            return None
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
    
    def __str__(self):
        if not self.isEmpty():
            elements = []
            frontNode = self.head
            while not frontNode is None:
                elements.append(frontNode.getData())
                frontNode = frontNode.getNext()
            print(elements)
        else:
            print("List is Empty")
    
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
            idx = None
        return idx
    
    def getItem(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.getNext()
        if curr is not None:
            return curr.getData()
        else:
            raise("Index out of range")
            
        
    def append(self, item):
        #adds item on the other end of list compared to add
        curr = self.head
        while curr.getNext() is not None:
            curr = curr.getNext()
        newNode = Node(item)
        newNode.setNext(curr.getNext())
        curr.setNext(newNode)
        
        
        
        
        
    def pop(self, index):
        self.remove(self.getItem(index))
        
#        if self.isEmpty():
#            print("Empty list")
#            return None
#        #single node
#        if self.head.getNext() is None:
#            frontNode = self.head
#            self.head = None
#            return frontNode
#        
#        current = self.head
#        previous = None
#        while current.getNext() is not None:
#            previous = current
#            current = current.getNext()
#        poppedNode = current
#        previous.next = current.getNext()
#        return poppedNode
    
    def slice(self, start, stop):
        newList = UnorderedList()
        i = stop - 1
        while i  >= start:
            newList.add(self.getItem(i))
            i-=1
        return newList
    
        
mylist = UnorderedList()

mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.append(99)
mylist.add(31)
mylist.add(77)
mylist.add(17)
#mylist.__str__()
#newList = mylist.slice(0, 3)
#newList.__str__()
#print(mylist.search(54))
print(mylist.index(99))