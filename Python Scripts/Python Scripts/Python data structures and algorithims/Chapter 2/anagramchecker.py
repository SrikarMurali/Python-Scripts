# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:51:47 2017

@author: Nathan
"""
from collections import Counter

def anagramSolution(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    c1 = [0] * 26
    c2 = [0] * 26
    print(c1)
    print(c2)
    
    for i in range(len(c1)):
        pos = ord(s1[i]) - ord('a')
        print(pos)
        c1[pos] = c1[pos] + 1
        
    for i in range(len(c2)):
        pos = ord(s2[i]) - ord('a')
        print(pos)
        c2[pos] = c2[pos] + 1
        
        
    if c1 != c2:
        return False
    return True

def anasol(s1, s2):
    return Counter(s1) == Counter(s2)


print(anasol('act', 'cat'))