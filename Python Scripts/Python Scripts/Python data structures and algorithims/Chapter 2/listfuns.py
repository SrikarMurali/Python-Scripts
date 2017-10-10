# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:33:59 2017

@author: Nathan
"""
import timeit
import random

#Programming Questions
#1

#t = list(range(10000))
#k = 10000
#def listindex(t, n):
#    
#    for i in range(k):
#        index = random.randint(0, k-1)
#        t[index]
#        
#
#for i in range(100000, 10000001, 1000000):
#    it = timeit.Timer("listindex(t," + str(i) + ")",
#                  "from __main__ import t, \
#                  listindex")
#    end_time = it.timeit(number = 10)
#    print("Time for %d index operations in a list of size %d"\
#          ": %16f seconds" % (k, i, end_time))
#    
    
#2
#dictionary = {}
#
#def dset(n):
#    global dictionary
#    for i in range(n):
#        dictionary[i] = i
#        
#def dget(n):
#    global dictionary
#    for i in range(n):
#        x = dictionary[i]
#
#print("Set times for a dictionary")
#for i in range(100000, 10000001, 1000000):
#    start_time = timeit.Timer("dset(" + str(i) + ")",
#                              "from __main__ import dset")
#    end_time = start_time.timeit(number = 10)
#    print("Time for {} dictionary insertions: {}".format(i, end_time))
#    print("Time for a single dictionary insert: {}".format(end_time/float(10 * i)))
#
#print("Get times for a dictionary")
#for i in range(100000, 10000001, 1000000):
#    start_time = timeit.Timer("dget(" + str(i) + ")",
#                              "from __main__ import dget")
#    end_time = start_time.timeit(number = 10)
#    print("Time for {} dictionary retrievals: {}".format(i, end_time))
#    print("Time for a single dictionary retrieval: {}".format(end_time/float(10 * i)))
#


#3
#t = []
#dictionary = {}
#def dictdelete(n):
#    global dictionary
#    dictionary = {i: i for i in range(n)}
#    for i in range(n):
#        del dictionary[i]
#        
#def listdelete(n):
#    global t
#    t = [i for i in range(n)]
#    for i in range(n - 1):
#        del t[0]
#
#
#for i in range(100000, 10000001, 1000000):
#    start_time = timeit.Timer("dictdelete(" + str(i) + ")",
#                              "from __main__ import dictdelete")
#    end_time = start_time.timeit(number = 10)
#    print("Time for {} dictionary deletions: {}".format(i, end_time))
#    print("Time for a single dictionary deletion: {}".format(end_time/float(i)))
#
#
#for i in range(100000, 10000001, 1000000):
#    start_time = timeit.Timer("listdelete(" + str(i) + ")",
#                              "from __main__ import listdelete")
#    end_time = start_time.timeit(number = 10)
#    print("Time for {} list deletions: {}".format(i, end_time))
#    print("Time for a single list deletion: {}".format(end_time/float(i)))

#4/5

def kthsmallest(tl, k):
    
    if len(tl) <= 10:
        tl.sort()
        return tl[k]
    
    pivotindex = random.randint(0, len(tl) - 1)
    pivot = tl[pivotindex]
    tl_greater = []
    tl_lesser = []
    tl_equal = []
    for item in tl:
        if item < pivot:
            tl_lesser.append(item)
        elif item > pivot:
            tl_greater.append(item)
        else:
            tl_equal.append(item)
            
    if k < len(tl_lesser):
        return kthsmallest(tl_lesser, k)
    elif k < len(tl_lesser) + len(tl_equal):
        return tl_equal[0]
    else:
        k_normalized = k - (len(tl_lesser) + len(tl_equal))
        return kthsmallest(tl_greater, k_normalized)
    
    

t = [random.randint(1, 20) for i in range(20)]
random.shuffle(t)
random.shuffle(t)
print(t)
kvalue = kthsmallest(t, 5)
print(kvalue)
sorted_t = sorted(t)
print(sorted_t)
print(sorted_t[5] == kvalue)
#for i in range(10000, 1000001, 20000):
#    t = timeit.Timer("random.randrange(%d) in x" %i,
#                     "from __main__ import random, x")
#    x = list(range(i))
#    lst_time = t.timeit(number = 1000)
#    x = {j:None for j in range(i)}
#    d_time = t.timeit(number=1000)
#    print("%d,%10.3f, %10.3f" % (i, lst_time, d_time))

#from timeit import Timer
#
#def test1():
#    l = []
#    for i in range(1000):
#        l = l + [i]
#
#def test2():
#    l = []
#    for i in range(1000):
#        l.append(i)
#        
#def test3():
#    l = [i for i in range(1000)]
#
#def test4():
#    l = list(range(1000))
#    
#
#
#t1 = Timer("test1()", "from __main__ import test1")
#print("concat ", t1.timeit(number = 1000), "milliseconds")
#
#t2 = Timer("test2()", "from __main__ import test2")
#print("append ", t2.timeit(number = 1000), "milliseconds")
#
#t3 = Timer("test3()", "from __main__ import test3")
#print("comprehension ", t3.timeit(number = 1000), "milliseconds")
#
#t4= Timer("test4()", "from __main__ import test4")
#print("list range ", t4.timeit(number = 1000), "milliseconds")
#
#popzero = Timer("x.pop(0)", "from __main__ import x")
#popend = Timer("x.pop", "from __main__ import x")
#
##x = list(range(2000000))
#
##x = list(range(2000000))
#
#print("pop(0)     pop()")
#
#for i in range(1000000, 100000001, 1000000):
#    x = list(range(i))
#    pt = popend.timeit(number=1000)
#    x = list(range(i))
#    pz = popzero.timeit(number=1000)
#    print("%15.5f, %15.5f" % (pz, pt))



'''chapter 2 questions
1. O(n^2)
2. O(n)
3. O(n)
4. O(n^3)
5. O(n)
6. O(n) '''
