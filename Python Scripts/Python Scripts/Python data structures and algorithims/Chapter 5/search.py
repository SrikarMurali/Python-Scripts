# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:35:17 2017

@author: Nathan
"""

import math
import random
import sys
import statistics

class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)
    
    def __len__(self):
        return self.size
    
    def __contains__(self, key):
        if self.get(key) != None:
            return True
        return False
    
  
    def printHashTable(self):
        for index in range(len(self.slots)):
            key = self.slots[index]
            value = self.data[index]
            print ("%d: %s:%s" % (index, key, value))

    def showSlots(self):
        print (self.slots)

    def showData(self):
        print (self.data)

    def hash_function(self, key, size):
        return key%size
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        index = start_slot
        while self.slots[index] is not None:
            if self.slots[index] == key:
                data = self.data[index]
                break
            else:
                index = self.rehash(index, len(self.slots))
                if index == start_slot:
                    break
        return data

    def put(self, key, data):
        hashVal = self.hash_function(key, len(self.slots))

        if self.slots[hashVal] is None:
            self.slots[hashVal] = key
            self.data[hashVal] = data
        elif self.slots[hashVal] == key:
            self.data[hashVal] = data   # replace
        else:
            next_slot = self.rehash(hashVal, len(self.slots))
            while self.slots[next_slot] is not None and \
                    self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data     # replace


def sequentialsearch(alist, item):
    i = 0
    while i < len(alist):
        if alist[i] == item:
            return True, item, i
        i+=1
    return False

def orderedsequentialsearch(alist, item):
    i = 0
    while i < len(alist):
        if alist[i] == item:
            return True, item, i
        if alist[i] > item:
            return False
        i+=1
    return False

def binarysearch(alist, item):
    first = 0
    last = len(alist) - 1
    
    while first <= last:
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

def recursivebinarysearch(alist, item, first, last):
    if first >= last:
        return False
    mid = math.floor((first + last)/2)
    if alist[mid] == item:
        return True
    elif alist[mid] < item:
        return recursivebinarysearch(alist, item, mid + 1, last)
    else:
        return recursivebinarysearch(alist, item, first, mid - 1)

def charhash(astring, tablesize):
    sumOfChars = 0
    for i in range(len(astring)):
        sumOfChars+= (i + 1)*ord(astring[i])
        print(sumOfChars)
    return sumOfChars%tablesize

def bubblesort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        print(passnum)
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist        

def shortbubblesort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum-=1
    return alist

def insertionsort(alist):
    for index in range(1, len(alist)):
        print(index, "i")
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position-=1
            print(position, "p")
        alist[position] = currentvalue
    return alist

def shellsort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        print(sublistcount)
        for startposition in range(sublistcount):
            gapinsertionsort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)
        
        sublistcount = sublistcount//2
    return alist

def gapinsertionsort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        
        currentvalue = alist[i]
        position = i
        print(currentvalue, position, gap)
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position-=gap
            print(position)
            
        alist[position] = currentvalue
        

def mergesort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)
        i,j,k = 0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i+=1
            else:
                alist[k] = righthalf[j]
                j+=1
            k+=1
            
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j+=1
            k+=1
    print("Merging ", alist)
    return alist


def merge_sort(alist, first, last):
    if first < last:
        mid = (first + last)//2
        merge_sort(alist, first, mid)
        merge_sort(alist, mid + 1, last)
        merge(alist, first, last)
    return alist

def merge(alist, first, last):
    mid = (first + last)//2
    
    leftside = alist[first:mid+1]
    rightside = alist[mid+1:last+1]
    leftside.append(sys.maxsize)
    rightside.append(sys.maxsize)
    
   
    i,j = 0,0
    
    for k in range(first, last + 1):
        if leftside[i] <= rightside[j]:
            alist[k] = leftside[i]
            i+=1
        else:
            alist[k] = rightside[j]
            j+=1
        



def quicksort(alist):
    quicksorthelper(alist, 0, len(alist) - 1)
    return alist

def quicksorthelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        
        quicksorthelper(alist, first, splitpoint - 1)
        quicksorthelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotindex = median(alist, first, last, (first+last)//2)
    alist[first], alist[pivotindex] = alist[pivotindex], alist[first]
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark+=1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark-=1
        
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    
    return rightmark

def median(a,i,j,k):
    if a[i] < a[j]:
        return j if a[j] < a[k] else k
    else:
        return i if a[i] < a[k] else k


def betterquicksort(alist):
    if len(alist) <= 1:
        return alist
    lesser, greater = [], []
    pivotval = medianof3s(alist)
    for item in alist:
        if item < pivotval:
            lesser.append(item)
        if item > pivotval:
            greater.append(item)
    lesser = betterquicksort(lesser)
    greater = betterquicksort(greater)
    
    return lesser + [pivotval] * alist.count(pivotval) + greater
    

def medianof3s(alist):
    vals = random.choices(alist, k = 3)
    print(vals)
    #ele2 = random.choice(alist)
    #ele3 = random.choice(alist)
    print(statistics.median(vals))
    return statistics.median(vals)
#alist = [76,53,23,64,23,65,86,662,898,2]
#alist = betterquicksort(alist)
#print(alist)
##H = HashTable()
#H[54] = "cat"
#H[26] = "dog"
#H[93] = "lion"
#H[17] = "tiger"
#H[77] = "bird"
#H[31] = "cow"
#H[44] = "goat"
#H[55] = "pig"
#H[20] = "chicken"
#del H[54]
#print(charhash('cat', 11))
#alist = [1,2,3,4,5,6]
#print(recursivebinarysearch(alist, 6, 8, 6))

#print(orderedsequentialsearch([1,2,3,4,5,6], 4.5))
#print(sequentialsearch([56,53,75,23,12,645,76], 76))