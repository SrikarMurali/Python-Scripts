# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:03:49 2017

@author: Nathan
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)
class CDLLwS(object):
    def __init__(self, nodeClass):
        self.head = None
        self.nodeClass = nodeClass

        self.sentinel = self.nodeClass(None)
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.len = 0
		
    def __len__(self):
        return self.len

    def __iter__(self):
        x = self.sentinel.next
        while x != self.sentinel:
            yield x
            x = x.next

    def __getitem__(self, i):
        if not -1 <= i < len(self):
            raise IndexError()
        elif i == 0:
            return self.sentinel.next
        elif i == -1:
            if len(self) > 0:
                return self.sentinel.prev
            else:
                raise IndexError()
        else:
            for j, x in enumerate(self):
                if j == i: return x

    def _insert_node(self, node, nextNode):
        node.prev = nextNode.prev
        node.next = nextNode
        node.prev.next = node
        node.next.prev = node
        self.len += 1

    def insert(self, i, node):
        self._insert_data(
                node,
                self.__getitem__(i, getNode=True) if len(self) > 0 else self.sentinel
        )

    def append(self, node):
        self._insert_node(
                node,
                self.sentinel
        )

    def pop(self, i=-1):
        x = self[i]

        x.prev.next = x.next
        x.next.prev = x.prev
		
        self.len -= 1
        return x

    def find(self, s, propName="data"):
        for x in self:
            if getattr(x, propName) == s:
                return x
        return None
    def __lt__(self,n1, n2):
       
        return n1.data < n2.data
    
    def __ge__(self, n1, n2):
        return n1.data >= n2.data
        
    def __str__(self):
        return str(map(lambda x:x.data, self))	
    def insertionSort(self, items):
        i = 1
        while i < items.len:
            j = i
            while j > 0:

                if self.__lt__(self.__getitem__(j), self.__getitem__(j-1)):
                    tmp = self.__getitem__(j)
                    jint = tmp.data
                    tmp.data = tmp.prev.data
                    tmp.prev.data = jint
                else:
                    break 
                j-=1
    
            i+=1
        return items
    
    def merge(self, first, second):
        #print('inside merge')
        if first is None or first is self.sentinel:
            return second
        if second is None or second is self.sentinel:
            return first
        print(first.data, second.data)
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
    
    def mergeSort(self, head):
#        if head is None or head is self.sentinel or head.next is None or head.next is self.sentinel:
            #return head
        if head is None or head is self.sentinel: 
            return head
        if head.next is None or head.next is self.sentinel:
            return head
         
        #print('here')
        second = self.split(head)
        #print('after split')
        head = self.mergeSort(head)
        second = self.mergeSort(second)
        
        return self.merge(head, second)
    
    def split(self, head):
        fast = slow = head
        print('fast1', fast.data)
        print('slow1', slow.data)
        while True:
            if  fast.next is None or fast.next is self.sentinel:
                print('inside fast.next')
                break
            if fast.next.next is None or fast.next.next is self.sentinel:
                print('inside fast.next.next')
                break
            fast = fast.next.next
            slow = slow.next
       
        print('slow', slow)
        print('slow.next', slow.next)
        temp = slow.next
        slow.next = None

        
        print('temp',temp.data)
        return temp
    def partition(self, left, head):
        
        #print('in partition')
        x = head.data
        i = left.prev
        j = left
        while j is not head:
            #print('j.data', j.data)
            if j.data <= x:
                if i is None:
                    i = left
                else:
                    i = i.next
                i.data, j.data = j.data, i.data
            j = j.next
        
        if i is None:
            i = left
        else:
            i = i.next
        i.data, head.data = head.data, i.data
        return i
    
    def quicksort(self, node):
        #print('in main quicksort')
        head = self.sentinel.prev
        #print(head, node)
        self.quicksortHelper(node, head)
        
    
    def quicksortHelper(self, left, head):
        #print('in helper')
        #print(head, head.next, left)
        if head is not None and left is not head and left is not head.next:
            temp = self.partition(left, head)
            #print(temp)
            self.quicksortHelper(left, temp.prev)
            self.quicksortHelper(temp.next, head)
    
    
    def selectionsort(self, head):
        node1 = head
        #print(node1.data)
        while node1 is not None and node1 is not self.sentinel:
            minval = node1
            node2 = node1
            while node2 is not None and node2 is not self.sentinel:
                if minval.data > node2.data:
                    minval = node2
                node2 = node2.next
            
            node1.data, minval.data = minval.data, node1.data
            node1 = node1.next

        return node1.next 
    
    def bubblesort(self, head):
        end = None
        swapped = True
        while swapped:
            curr = head
            print('curr head', curr.data)
            swapped = False

            while curr is not end and curr.next is not self.sentinel:
                print('curr', curr.data)
                print('curr.next.data', curr.next.data)

                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = True
                curr = curr.next
            end = curr
            print('end.data', end.data)
    
    def shellsort(self, gap, head, items):
        
        
        k = gap
        while k > 1:
            for i in range(k, items.len):
                temp = self.__getitem__(i)
#                print('temp.data', temp.data)
                j = i
                while j >= k and self.__getitem__(j-k).data > temp.data:
                    x = self.__getitem__(j)
                    y = self.__getitem__(j-k)
                    x.data, y.data = y.data, x.data
#                    print('x.data', x.data)
#                    print('y.data', y.data)
                    j-=k
                z = self.__getitem__(j)
#                print('z.data', z.data)
#                print('temp2.data', temp.data)
                z.data, temp.data = temp.data, z.data
            k//=2
            if k == 1:
                self.insertionSort(items)
    def printList(self, node):
        temp = node
        print("Forward Traversal using next poitner")
        while(node is not None):
            print(node.data,)
            temp = node
            node = node.next
        print("\nBackward Traversal using prev pointer")
        while(temp):
            print(temp.data,)
            temp = temp.prev
x = CDLLwS(Node)
for i in range(1,50):
    j = Node(random.randint(1,20))
    x.append(j)
#x.append(Node(3))
#x.append(Node(4))
#x.append(Node(20))
#x.append(Node(5))
#x.append(Node(7))
#x.append(Node(12))
#x.append(Node(9))
#x.append(Node(18))
#x.append(Node(21))
#x.append(Node(25))
#x.append(Node(19))
#x.append(Node(37))
#for elem in x:
#   print(elem)

#print(x.sentinel)
y = CDLLwS(Node)
#print('sent',x.sentinel.next)
#print(x.sentinel.prev)
#print('starting quicksort')
#x.quicksort(x.sentinel.next)
#for elem in x: # for quicksort do not assign to y
#    print(elem)
#x.printList(x.sentinel)
#x.insertionSort(x)
x.shellsort(x.len//2, x.sentinel.next, x)
for elem in x:
    print(elem)

#for quick sort and insertion sort use for i in x

#for mergesort use the printlist function
