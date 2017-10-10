# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:48:20 2017

@author: Nathan
"""

import math
from Queue import Queue

def rsort(n):
    '''(list of int) -> list of int
    '''
    bin_list = [Queue for _ in range(10)]
    max_digits = int(math.ceil(math.log(max(n), 10))) # calculate # of digits

    for k in range(max_digits):
        for num in n:
            sig_dig = num // 10**k % 10 # find digit's value
            bin_list[sig_dig].enqueue(int(num))

        n = [] # we can reuse the name `n`, rather than using a different name
        for bins in bin_list:
            while not bins.is_empty(): # loop to dequeue all values
                n.append(bins.dequeue())

    return n # the return statement is outside the loop!

        
 

            
   
print(rsort([123,433,12,434,67,232,98,33]))            
            
    
        
    