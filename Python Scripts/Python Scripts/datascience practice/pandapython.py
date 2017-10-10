# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:38:44 2017

@author: Nathan
"""

import pandas as pd
import numpy as np
import string
from numpy.random import randn

my_dict = {"Seattle": 652405, "Spokane": 210721, "Bellevue": 133992, "Leavenworth": 1992}
ser = pd.Series(my_dict)
print(ser)

data = list([1,2,3,4])
ser = pd.Series(data)
print(ser)

data = np.random.randn(5)
ser = pd.Series(data)
print(ser)

alpha = list(string.ascii_lowercase[:5])
data = np.random.randn(5)
ser = pd.Series(data, index=alpha)
print(ser)

ser = pd.Series(my_dict)
print(ser)
ser.name = "Population"
ser.index.name = "City"
print("After naming the data and index")
print(ser)
y_dict = {"Seattle": 652405, "Spokane": 210721, "Bellevue": 133992, "Leavenworth": 1992}
ser = pd.Series(my_dict)
print(ser)
# attributes
print("ser.shape:%s" %(str(ser.shape)))
print("ser.dtype:%s" %(str(ser.dtype)))
# methods
print("ser.mean():%s" %(str(ser.mean())))
# numpy ufuncs
print("np.mean(ser):%s" %(str(np.mean(ser))))
# vectorization
print("np.sqrt(ser):\n%s" %(str(np.sqrt(ser))))
print("ser + ser:\n%s" %(str(ser + ser)))
print("ser * 10:\n%s" %(str(ser * 10)))
# indeing
print("Indexing ser[0]:%s" %(str(ser[0])))
print("Indexing ser[[0, 2]]:\n%s" %(str(ser[[0, 2]])))
print("Boolean indexing ser[[ser > ser.median()]]:\n%s" %(str(ser[ser > ser.median()])))
print("Slicing ser[0:2]:\n%s" %(str(ser[0:2])))
print("Slicing ser[2:]:\n%s" %(str(ser[2:])))





#Dataframe

washington = ["Seattle", "Spokane", "Tacoma", "Vancouver"]
idaho = ["Boise", "Nampa", "Meridian", "Idaho Falls"]
oregon = ["Portland", "Eugene", "Salem", "Gresham"]
pops = [washington, idaho, oregon]
df = pd.DataFrame(pops)
print(df)
df = pd.DataFrame(pops, index=["WA", "ID", "OR"], columns=np.arange(1, len(washington) + 1))
print("Population DataFrame #1")
print(df)


pops_dict = {"WA": washington, "ID": idaho, "OR": oregon}
df2 = pd.DataFrame(pops_dict)
print(df2)
df2.index+=1
print("Population DataFrame #2")
print(df2)

df2T = df2.T
df = df.sort_index()
print(df)
print(df2T)
print(df == df2T)

washington = {"Seattle": 652405, "Spokane": 210721, "Bellevue": 133992, "Leavenworth": 1992}
idaho = {"Boise": 205671, "Nampa": 81557, "Coeur d'Alene": 44137, "Moscow": 23800}
oregon = {"Portland": 583776, "Eugene": 156185, "Hillsboro": 91611, "Corvallis": 54462}
pops = {"WA": washington, "ID": idaho, "OR": oregon}
df = pd.DataFrame(pops)
print(df)

rand_data = randn(3,4)
rand_df = pd.DataFrame(rand_data, index = ["a","b", "c"], columns = ["col1", "col2", "col3", "col4"])
print(rand_df)


print(rand_df["col2"])
rand_df["col4"] = 100
print(rand_df)

rand_df["col5"] = rand_df["col1"] > rand_df["col2"]
print(rand_df)
rand_df["sum"] = rand_df.sum(axis="columns")
print(rand_df)

rand_df.insert(2, "ones", 1)
print(rand_df)

del rand_df["col5"]
print(rand_df)
sum_ser = rand_df.pop("sum")
print(rand_df)
print("Popped column is a Series:")
print(sum_ser)


rand_data = randn(3, 4)
rand_df = pd.DataFrame(rand_data, index=["a", "b", "c"], columns=["col1", "col2", "col3", "col4"])
print(rand_df)

print(rand_df.loc["b"])
print(rand_df.iloc[1])
print(rand_df[0:2])

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']},
index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
'B': ['B4', 'B5', 'B6', 'B7'],
'C': ['C4', 'C5', 'C6', 'C7'],
'D': ['D4', 'D5', 'D6', 'D7']},
index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
'B': ['B8', 'B9', 'B10', 'B11'],
'C': ['C8', 'C9', 'C10', 'C11'],
'D': ['D8', 'D9', 'D10', 'D11']},
index=[8, 9, 10, 11])

frames = [df1, df2, df3]
result = pd.concat(frames)
print(result.tail(2))
print(help(result.tail))

print(result.describe())
print("\n")
print(result.head(n=2))
print("\n")
print(result.tail(n=2))

fname = r"files\results_df.csv"
result.to_csv(fname)

