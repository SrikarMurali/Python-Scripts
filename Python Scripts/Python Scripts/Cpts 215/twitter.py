# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:16:48 2017

@author: Nathan
"""

import sys
from scanner import Scanner
from datetime import datetime as dt

def read_records(file):
    s = Scanner(file)
    lst = []
    i = 0
    for line in file:
        x = s.readline().rstrip()
        lst.append(x[1:])
        i+=1
    lst = list(filter(None, lst))
    return lst

def create_record(scan):
    x = scan.readline()
    x = x[1:]
    y = list()
    y.append(x)
    return y

def is_more_recent(rec1, rec2):
    idx1 = rec1.index('20')
    idx2 = rec2.index('20')
    date1 = rec1[idx1:len(rec1)]
    date2 = rec2[idx2:len(rec2)]
    lst1 = list(date1.split())
    lst2 = list(date2.split())
    
    i = 0
    while i < 4:
        if ':' in lst1[i]:
            time = lst1[i].split(':')
            
            seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
            lst1[3] = seconds
        if ':' in lst2[i]:
            time = lst2[i].split(':')   
            seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
            lst2[3] = seconds
        if int(lst1[i]) > int(lst2[i]):
           return rec1
        elif int(lst1[i]) < int(lst2[i]):
            return rec2
        else:
            i+=1
        
def merge_and_sort(lst1, lst2):
    fin = []
    #lst1 = lst1[::-1]
    #lst2 = lst2[::-1]
    
    i,j = 0, 0
    total = len(lst1) + len(lst2)
#    while lst1 and lst2:
#        if is_more_recent(lst1[0], lst2[0]) == lst1[0]:
#            print(lst1.pop(0))
#            fin.append(lst1.pop(0))
#        else:
#            print(lst2.pop(0))
#            fin.append(lst2.pop(0))
#    
#    return fin + lst1 + lst2
    while len(fin) != total:
        if len(lst1) == i:
            fin+= lst2[j:]
            break
        elif len(lst2) == j:
            fin+=lst1[i:]
        elif is_more_recent(lst1[i], lst2[j]) == lst1[i]:
            fin.append(lst1[i])
            i+=1
        else:
            fin.append(lst2[j])
            j+=1
    return fin
        
def write_records(lst):
    file = open('sorted_demo.txt', 'w')
    for item in lst:
        file.write("%s\n" % item)
        
def main():
    print('reading...')
    lst1 = read_records('tweet1_demo.txt')
    lst2 = read_records('tweet2_demo.txt')
    if len(lst1) > len(lst2):
        print('tweet1_demo.txt has the most tweets', len(lst1))
    else:
        print('tweet1_demo.txt has the most tweets', len(lst1))
    print('merging...')
    lst = (merge_and_sort(lst1, lst2))
    print('writing...')
    write_records(lst)
    print(lst)
    lst = lst[::-1]
    for i in range(5):
        idx = lst[i].index('20')
        print(lst[i][:idx])

if __name__ == "__main__":
    main()     
    
#lst1 = read_records('tweet1_demo.txt')
#lst2 = read_records('tweet2_demo.txt')
#lst = (merge_and_sort(lst1, lst2))
#print(lst)
#st = '2013 10 1 13:46:42'
#lst = st.split()
#print(lst)
#x = lst[3].split(':')
#time = int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2])
#lst[3] = time
#print(lst)
#print(is_more_recent('@poptardsarefamous "Sometimes I wonder 2 == b or !(2 == b)" 2013 10 1 13:46:42','@pythondiva "My memory is great <3 64GB android" 2013 10 1 10:36:11'))