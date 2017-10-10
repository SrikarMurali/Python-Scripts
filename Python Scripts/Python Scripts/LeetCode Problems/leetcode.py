# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:00:37 2017

@author: Nathan
"""
import math
import collections

def sums(nums, target):
    
    for i in len(nums):
        j = target - nums[i]
        if j in nums:
            return (i, j)
    return None

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        newNum = 0
        remainder = 0
        if x < 0:
            return -1*reverse(-x)
        while (x!=0):
            remainder = x%10
            newNum = newNum*10 + remainder
            x = x//10
        return newNum

def rom_to_int(string):

    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:


        continueyes=True

        while continueyes:
            if len(string)>=len(pair[0]):

                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    print((pair[0]))
                    #print(string[len(pair[0]):])
                    string=string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False

    return returnint
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or strs is None:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        minString = strs[0]
        minLen = len(minString)
        for i in range(len(strs)):
            if len(strs[i]) < minLen:
                minLen= len(strs[i])
        
        for i in range(minLen):
            for j in range(len(strs) - 1):
                s1 = strs[j]
                s2 = strs[j+1]
                if s1[i] != s2[i]:
                    return s1[:i]
        return strs[0][0:minLen]
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                del nums[i]
                i-=1
            i+=1
        print(nums)
        return len(nums) 
def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low
def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = len(digits) - 1
        if digits[end] != 9:
            digits[end] = digits[end] + 1
            return digits
        if len(digits) == 1:
            if digits[0] == 9:
                digits.insert(0, 1)
                digits[1] = 0
            else:
                digits[0] = digits[0] + 1
        for i in range(len(digits) - 1, -1, -1):
            print(i)
            if digits[i] == 9:
                digits[i] = 0
                continue
            digits[i] = digits[i] + 1
        return digits
    
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        s = s.lower()
        result = []
        for i in range(len(s)):
            for j in range(0,i):
                substr = s[j:i+1]
                if substr == substr[::-1]:
                    result.append(substr)
        if len(result) == 0:
            return s[0]
        
        palindromeIndex = 0
        for i in range(len(result)):
            if len(result[i]) > len(result[palindromeIndex]):
                palindromeIndex = i
            
        return palindromeIndex, result
def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        s = 0
        while num > 0:
            s = s + num%10
            num//=10
        if s > 9:
            s = addDigits(s)
        return s   
                
                

def is_prime(n):
    for i in range(2, int(math.ceil(math.sqrt(n))+1)):
            if n%i == 0:
                return False
    return True

def sum_primes(n):
    return sum([x for x in range(2, n+1) if is_prime(x)])

def longestPalindrome(s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    print(odds)
    print(bool(odds))
    x = len(s) - odds + bool(odds)
    print(x)
    return x
#n = int(input("Please enter a number: "))
#print(is_prime(n)) 
#print(sum_primes(n))
s = 'bbcc'
longestPalindrome(s)
x = [[5] + i for i in [4,3,1,2]]
print(x)
#print(plusOne(nums))
#print(removeDuplicates(nums))
#print(longestCommonPrefix(strs))
#print(rom_to_int('MCMXCVI'))
#nums = [4,5,2,3,7,8,1]
#print(sums(nums, 7))
#print(reverse(-3353))