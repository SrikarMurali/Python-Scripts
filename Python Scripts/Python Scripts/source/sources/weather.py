# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 11:36:23 2017

@author: Nathan
"""

import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")

for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)




