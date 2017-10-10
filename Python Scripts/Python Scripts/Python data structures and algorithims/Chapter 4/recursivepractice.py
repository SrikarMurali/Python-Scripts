# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:24:30 2017

@author: Nathan
"""

import random
import math
from Stack import Stack
from turtle import *

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        currentCoin = coinsUsed[coin]
        print(currentCoin)
        coin-=currentCoin
    
    
    
    
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)
        
def moveDisk(fromPole, toPole):
    print("moving disk form %d to %d\n" % (fromPole, toPole))

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()
    
def getMid(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                    degree - 1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                    degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                    degree - 1, myTurtle)
        

def drawSpiral(myTurtle, linelen):
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        drawSpiral(myTurtle, linelen - 5)
    

def recursivesum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + recursivesum(numlist[1:])


def tree(branchlen, t):
    if branchlen > 5:
        if branchlen > 20:
            t.color('red')
        ang = random.randrange(15,40)
        reduce = random.randrange(5, 20)
        t.forward(branchlen)
        t.right(ang)
        tree(branchlen - reduce, t)
        t.left(2 * ang)
        tree(branchlen - reduce, t)
        t.right(ang)
        t.backward(branchlen)
        t.color("green")

def snowflake(t, length, depth):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    t.color(colormap[random.randrange(6)])
    if depth == 0:
        t.forward(length)
    else:
       
        length/=3
        depth-=1
        snowflake(t, length, depth)
        t.right(60)
        snowflake(t, length, depth)
        t.left(120)
        snowflake(t, length, depth)
        t.right(60)
        snowflake(t, length, depth)

def hilbert(t, size, depth, ang):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    if depth == 0:
        return None
    t.color(colormap[random.randrange(6)])
    t.right(ang)
    hilbert(t, size, depth - 1, -ang)
    t.forward(size)
    t.left(ang)
    hilbert(t, size, depth - 1, ang)
    t.forward(size)
    hilbert(t, size, depth - 1, ang)
    t.left(ang)
    t.forward(size)
    hilbert(t, size, depth - 1, -ang)
    t.right(ang)
    
def toStr(n, base):
    conversionString = "0123456789ABCDEF"
    if n < base:
        return conversionString[n]
    else:
        return toStr(n//base, base) + conversionString[n%base]

def toStrStackEx(n, base):
    conversionString = "0123456789ABCDEF"
    s = Stack()
    if n < base:
        s.push(conversionString[n]) 
    else:
        s.push(conversionString[n % base])
        toStrStackEx(n // base, base)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def reverse(lst):
    if len(lst) == 1:
        return lst
    
    reverselist = reverse(lst[1:])
    reverselist.append(lst[0])
    return reverselist  

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def jugs(jug1, jug2, amount):
    biggerJug = max(jug1, jug2)
    smallerJug = min(jug1, jug2)
    amountInBig = 0
    amountInSmall = 0
    amountInBig+=biggerJug
    amountInSmall+=smallerJug
    amountInBig-=smallerJug
    amountInSmall = 0
    amountInSmall+=amountInBig
    amountInBig = 0
    amountInBig+=biggerJug
    amountInBig = amountInBig - (smallerJug - amountInSmall)
    return amountInBig == amount

def cannibalsandmissionaries():
    cannibals = 3
    missionaries = 3
    cannibals2 = 0
    missionaries2 = 0
    cannibals2+=1
    missionaries2+=1
    cannibals-=1
    missionaries-=1
    missionaries+=1
    missionaries2-=1
    cannibals-=1
    cannibals2+=1
    missionaries2+=2
    missionaries-=2
    cannibals2+=1
    missionaries2+=1
    missionaries-=1
    cannibals-=1
    
    return ((cannibals == 0 and cannibals2 == 3) and (missionaries == 0 and \
           missionaries2 == 3))


def combo(num, rows):
    return int((math.factorial(num)) / ((math.factorial(rows)) * math.factorial(num - rows)))

def recursiveCombo(num, rows):
    if rows == 0 or rows == num:
        return 1
    return recursiveCombo(num - 1, rows - 1) + recursiveCombo(num - 1, rows)

def recursivePascal(rows):
    for row in range(rows):
        end = ""
        for col in range(row + 1):
            end = end + str(recursiveCombo(row, col)) + "\t"
            print(end)
        print(end)
        
def pascal(rows):
    triangle = []
    
    for count in range(rows):
        curr_row = []
        
        for element in range(count + 1):
            curr_row.append(combo(count, element))
        triangle.append(curr_row)
        
    return triangle

#recursivePascal(5)
#for row in pascal(5):
#    print(row)
#t = Turtle()
#myWindow = t.getscreen()
##t.penup()
##t.setposition(-150,-150)
##t.speed(10)
#hilbert(t, 10, 5, 90)
#t.pendown()
#t.color("blue")
#t.speed(10)
#for i in range(3):
#    snowflake(t, 600, 3)
#    t.left(120)
#
print(toStr(255,2))
#myWindow.exitonclick()


#print(cannibalsandmissionaries())
#print(jugs(7,4,6))
#myPen = Turtle()
#myPen.speed(10)
#myPen.color("#000000")
#
#
## This function draws a box by drawing each side of the square and using the fill function
#def box(boxSize):
#    while boxSize > 0:
#        myPen.begin_fill()
#        # 0 deg.
#        myPen.forward(boxSize)
#        myPen.left(90)
#        box(boxSize + 5)
#        # 90 deg.
#        myPen.forward(boxSize)
#        myPen.left(90)
#        box(boxSize + 10)
#        # 180 deg.
#        myPen.forward(boxSize)
#        myPen.left(90)
#        box(boxSize + 5)
#        # 270 deg.
#        myPen.forward(boxSize)
#        myPen.end_fill()
#        myPen.setheading(0)
#	
#
##Position myPen in center of the screen
#myPen.penup()
#myPen.goto(-50,-50)
#myPen.pendown()
#
##draw the first box
#box(1000)
#def jugs(jug1, jug2, wateramount):
    
#print(fibonacci(10))
#print(reverse([5,6,8,9,7,1]))
#print(factorial(7))
#c1 = [1,5,10,21,25]
#coinsUsed = [0] * 64
#coinCount = [0] * 64
#print(dpMakeChange(c1, 63, coinCount, coinsUsed))
#printCoins(coinsUsed, 63)        
#printCoins(coinsUsed, 63)
#print(coinsUsed)
#moveTower(5,1,2,3)
#myTurtle = Turtle()
#myWindow = myTurtle.getscreen()
#myTurtle.left(90)
#myTurtle.up()
#myTurtle.backward(100)
#myTurtle.down()
#myTurtle.color("green")
#myTurtle.speed(0)
#tree(75, myTurtle)
#myWindow.exitonclick()
#myPoints = [(-500, -250), (0,500), (500, -250)]
#sierpinski(myPoints,5, myTurtle)
#myWindow.exitonclick()
#drawSpiral(myTurtle, 100)
#print(toStrStackEx(255, 2))
#2wprint(recursivesum([1,2,3,4,5,6]))

