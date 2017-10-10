# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:29:11 2017

@author: Nathan
"""
import Stack
import operator

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.left.preorder()
        if self.rightChild:
            self.right.preorder()

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    sVal = ""
    if tree.getLeftChild() and tree.getRightChild():
        sVal+= '(' + printexp(tree.getLeftChild())
        sVal+=str(tree.getRootVal())
        sVal+= printexp(tree.getRightChild()) + ')' 
        print(sVal)
    else:

        sVal+=str(tree.getRootVal())

    return sVal

def buildParseTree(fpexp):
    oper = ['+', '-', '*', '/', '//', 'and', 'or', 'not']
    fplist = fpexp.replace(' ', '').split()
    pStack = Stack.Stack()
    eTree = BinaryTree(' ')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in oper:
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in oper:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return eTree

def postordereval(tree):
    opers = {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    result1 = None
    result2 = None
    if tree:
        result1 = postordereval(tree.getLeftChild())
        result2 = postordereval(tree.getRightChild())
        if result1 and result2:
            return opers[tree.getRootVal()](result1, result2)
        else:
            return tree.getRootVal()
            
def evaluate(parseTree):
    opers = {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv,
             'and':operator.and_, 'or':operator.or_, 'not':operator.not_}
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    
    if leftChild and rightChild:
        func = opers[parseTree.getRootVal()]
        return func(evaluate(leftChild), evaluate(rightChild))
    else:
        return parseTree.getRootVal()



x = BinaryTree('+')
x.insertLeft('3')
x.insertRight('*')
l = x.getRightChild()
l.insertLeft(4)
l.insertRight(5)
#l = x.getRightChild()
#l.insertRight('*')
#x = buildParseTree('((4*5) + 3)')
#print(postorder(x))
#x.insertRight(3)
#print(postordereval(x))
print(printexp(x))
#
#print(postordereval(x))

#print(buildParseTree('3+(4*5) or (2+3)').getRootVal())
#r = BinaryTree('a')
#print(r.getRootVal())
#
#print(r.getLeftChild())
#r.insertLeft('b')
#
#print(r.getLeftChild())
#
#print(r.getLeftChild().getRootVal())
#
#r.insertRight('c')
#print(r.getRightChild())
#
#print(r.getRightChild().getRootVal())
#
#r.getRightChild().setRootVal('hello')
#print(r.getRightChild().getRootVal())



#def BinaryTree(r):
#    return [r, [], []]
#
#def insertLeft(root, newBranch):
#    t = root.pop(1)
#    if len(t) > 1:
#        root.insert(1, [newBranch, t, []])
#    else:
#        root.insert(1, [newBranch, [], []])
#    return root
#
#def insertRight(root, newBranch):
#    t = root.pop(2)
#    if len(t) > 1:
#        root.insert(2, [newBranch, [], t])
#    else:
#        root.insert(2, [newBranch, [], []])
#    return root
#
#def getRootVal(root):
#    return root[0]
#
#def setRootVal(root, newVal):
#    root[0] = newVal
#
#def getLeftChild(root):
#    return root[1]
#
#def getRightChild(root):
#    return root[2]