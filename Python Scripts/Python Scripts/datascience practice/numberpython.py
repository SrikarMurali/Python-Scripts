# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:54:04 2017

@author: Nathan
"""

import numpy as np
from numpy.random import randn

x = list(range(11))
print(x)

x = np.array(x)
print(x)

x = [[1,2,3], [4,5,6]]
print(x)
x = np.array(x)
print(x)
print("Number of dimensions: %d" %(x.ndim))
print("Shape (rows, cols): %s" %(str(x.shape)))
print("Datatype of items: %s" %(x.dtype))

x_floats = x.astype(np.float)
print(x_floats)
print("Datatype of items: %s" %(x_floats.dtype))

x = np.arange(0, 11)
print(x)

x1 = np.arange(10)
print(x1)

x2 = np.ones(10)
print(x2)

x3 = np.zeros(10)
print(x3)

x4 = np.full(10, 5.0)
print(x4)

x = range(11)
y = range(10, 21)
z = []
for i in range(len(x)):
    z.append(x[i] + y[i])
print(z)

x = np.arange(11)
y = np.arange(10, 21)
z = z + y
print(z)

x = np.arange(10)
print(x)
x+=1
print(x)

x = np.arange(11)
x *= np.array([2])
print(x)

m_names = np.array(["Mary", "Michael", "Margaret", "Mary", "Marcus", "Molly"])
m_ages =  np.array([28    , 72       , 12        , 34    , 40      , 68])
mary_marcus = (m_names == "Mary") | (m_names == "Marcus")
print(m_names)
print(mary_marcus)

print(m_ages[mary_marcus])

x = np.arange(10)
print(x)
print(x[3])

ones = np.ones((2,3))
print(ones[0][0])
print(ones[0, 0])

rand_data = randn(3,4)
print(rand_data)
rand_data[2][0] = 100
print(rand_data)

negatives = rand_data < 0
print(negatives)
rand_data[negatives] = 0
print(rand_data)

x_list = list(range(10))
print("x_list: %s" %(x_list))
chunk = x_list[3:7]
print("chunk: %s" %(chunk))
chunk[0] = 50
print("chunk: %s" %(chunk))
print("x_list: %s" %(x_list))

x = np.arange(10)
print(x)
print("x: %s" %(x))
chunk = x[3:7]
print("chunk: %s" %(chunk))
chunk[0] = 50
print("chunk: %s" %(chunk))
print("x: %s" %(x))
x[2:5] = 100
print(x)

x = np.arange(10)
print(x)
print("x: %s" %(x))
chunk = x[3:7].copy()
print("chunk: %s" %(chunk))
chunk[0] = 50
print("chunk: %s" %(chunk))
print("x: %s" %(x))


ints = np.arange(10)
print(ints.shape)
print(ints)
ints = ints.reshape(5, 2)
print(ints.shape)
print(ints)


x = np.arange(6).reshape((2,3))
print(x)
print(x.shape)
x_t = x.T
print(x_t)
print(x_t.shape)


nums = np.arange(10)
print(nums)
print(np.sqrt(nums))

nums2 = np.random.randn(4,4)
print(nums2)
print(np.absolute(nums2))


nums = np.arange(5)
print(nums)
powers = np.full(5,2.0)
powers[-1] = 3
print(powers)
nums2 = np.arange(5) + 1

print(np.power(nums, powers))
print(np.power(nums, nums2))
print(nums)
print(nums2)
print(np.maximum(nums, nums2))