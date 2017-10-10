# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import gcd

class Fraction:
    def __init__(self, top, bottom):
        try:
            common = gcd(top, bottom)
            self.num = top//common
            self.den = bottom//common
        except TypeError:
            print("Not an integer")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__str__)
    
    def show(self):
        print(self.num, "/", self.den)
        
    @property
    def getDen(self):
        return self.den
    
    @property
    def getNum(self):
        return self.num
    
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
    
    def __radd__(self, other):
        if other == 0:
            return self
        otherfraction = Fraction(other, 1)
        newnum = self.num * otherfraction.den + \
                self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
    
    def __iadd__(self, other):
        self.num = self.num * other.den + self.den * other.num
        self.den = self.den * other.den
        return self
    
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - \
                self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
    
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
    
    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum
    
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum
    
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum
    
   
    
  
    
fract = Fraction(45, 90)
fract2 = Fraction(60, 90)
fract3 = Fraction(60, 90)
print(fract3 + fract2)
