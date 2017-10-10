# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:20:43 2017

@author: Nathan
"""
import string

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    

def superPalinChecker(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]    

def parChecker(symstr):
    a = Stack()
    
    bal = True
    idx = 0
    while idx < len(symstr) and bal:
        sym = symstr[idx]
        
        if sym in "([{":
            a.push(sym)
        else:
            if a.isEmpty():
                bal = False
            else:
                top = a.pop()
                if not matches(top, sym):
                    bal = False
        idx += 1
    
    if bal and a.isEmpty():
        return True
    else:
        return False

def matches(opener, closer):
    o = "([{"
    c = ")]}"
    
    return o.index(opener) == c.index(closer)


def divideby2(num):
    remainder = Stack()
    
    while num > 0:
        rem = num % 2
        remainder.push(rem)
        num//=2
    
    binarystring = ""
    while not remainder.isEmpty():
        binarystring+= str(remainder.pop())
    
    return binarystring


def baseconverter(num, base):
    digits = "0123456789ABCDEF"
    
    remainder = Stack()
    
    while num > 0:
        rem = num % base
        remainder.push(rem)
        num//=base
    
    end_string = ""
    while not remainder.isEmpty():
        end_string+= digits[(remainder.pop())]
    
    return end_string

def infixtopostfix(infixexpr):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
     
    operands = Stack()
    postfix_endlist = []
     
    tokenlist = infixexpr.split()
    if not checker():
        return "Invalid infix expression"
    
    for token in tokenlist:
        if token in string.ascii_uppercase:
            postfix_endlist.append(token)
        elif token == '(':
            operands.push(token)
        elif token == ')':
            top_token = operands.pop()
            while top_token != '(':
                postfix_endlist.append(top_token)
                top_token = operands.pop()

        else:
            while (not operands.isEmpty()) and \
                (precedence[operands.peek()] >= precedence[token]):
                    postfix_endlist.append(operands.pop())
            
            operands.push(token)
        
    while not operands.isEmpty():
        postfix_endlist.append(operands.pop())
        
    return " ".join(postfix_endlist)


def postfixeval(postfixexpr):
    if not checker(postfixexpr):
        return "Invalid postfix expression"
    
    operands = Stack()
    
    tokenlist = postfixexpr.split()
    
    for token in tokenlist:
        if token in "0123456789":
            operands.push(int(token))
        else:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = domath(token, operand1, operand2)
            operands.push(result)
    return operands.pop()

def domath(token, operand1, operand2):
    if token == "*":
        return operand1 * operand2
    elif token == "/":
        return operand1 / operand2
    elif token == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2


def infixevaluator(infixexpr):
    operators = Stack()
    operands = Stack()
    valid = ["+", "-", "/", "*", "^"]
    infixexpr = infixexpr.replace(" ", "")
    infixexpr+= " "
    print(infixexpr)
    for i in infixexpr:
        if i in "0123456789":
            operands.push(int(i))
        if i in valid:
            operators.push(i)
        if i == ")" or i == " ":
                while not operators.isEmpty():
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    operator = operators.pop()
                    print(operand1, operator, operand2)
                    result = domath(operator, operand1, operand2)
                    operands.push(result)
    return operands.pop()



def checker(infixexpr):
    if not infixexpr:
        return False
    valid = ["(", ")", "+", "-", "/", "*", "^"]
    infixexpr = infixexpr.strip()
    parenlist = []
    tokens = infixexpr.split(" ")
    cleantokens = []
    for i in infixexpr:
        if i == "(" or i == ")":
            parenlist.append(i)
    parentheses = ''.join(parenlist)
    if not parChecker(parentheses):
        return False
    
    for i in tokens:
        i = i.strip()
        cleantokens.append(i)
        if i not in valid and not i.isdigit():
            return False
    
    return cleantokens

print(superPalinChecker("I PREFER PI"))            
#print(infixevaluator("5 + 4 * 3"))
#print(postfixeval(" 4 5 6 * + "))
#print(postfixeval(" 7 8 + 3 2 + /"))
#
#print(infixtopostfix("( A + B ) * ( C + D )"))    
#print(infixtopostfix("( A + B ) * C"))    
#print(infixtopostfix("A + B * C"))    
#
#    
#     
#print(divideby2(255))
#print(baseconverter(233, 8))
#print(baseconverter(233, 16))
#print(parChecker("({[]})"))
