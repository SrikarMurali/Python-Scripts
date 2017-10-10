# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:41:37 2017

@author: Nathan
"""
import math

class BinaryHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0
    
    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i//=2
    
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)
    
    def percDown(self, i):
        while  (i * 2) <= self.currentSize:
            percNode = self.minChild(i)
            if self.heapList[i] > self.heapList[percNode]:
                self.heapList[i], self.heapList[percNode] = self.heapList[percNode], self.heapList[i]
            i = percNode
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize - 1]
        self.currentSize-=1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i-=1
   
        
    def heapify(self,alist,end,i):
        left=2 * i 
        right=2 * i + 1  
        largest=i   
        if left < end and alist[i] < alist[left]:   
            largest = left   
        if right < end and alist[largest] < alist[right]:   
            largest = right   
        if largest != i:   
            alist[i], alist[largest] = alist[largest], alist[i]   
            self.heapify(alist, end, largest) 
        
            
    def sortHeap(self,alist):
        end = len(alist)   
        
        for i in range(end//2-1, -1, -1):   
            self.heapify(alist, end, i)   
        for i in range(end-1, 0, -1):
            print(alist[i])
            alist[i], alist[0] = alist[0], alist[i]   
            self.heapify(alist, i, 0)
        return alist
        


  
class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0,0)]
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.percDown(i)
            i = i - 1
                        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
               tmp = self.heapArray[i//2]
               self.heapArray[i//2] = self.heapArray[i]
               self.heapArray[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            
    def __contains__(self,vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False
        

b = BinaryHeap()
alist = [2, 7, 1, -2, 56, 5, 3]
b.buildHeap(alist)
#print(b.heapList)
print(b.sortHeap(b.heapList))
#print(b.heap_sort(b.heapList))

#a = b.s.ortHeap(alist)
#print(a)