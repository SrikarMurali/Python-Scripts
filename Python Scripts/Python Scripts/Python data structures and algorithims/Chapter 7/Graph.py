# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:34:01 2017

@author: Nathan
"""
import pprint
import Queue
import Stack
import sys
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices+=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, fromNode, toNode, cost=0):
        if fromNode not in self.vertList:
            newVertex = self.addVertex(fromNode)
        if toNode not in self.vertList:
            newVertex = self.addVertex(toNode)
        self.vertList[fromNode].addNeighbor(self.vertList[toNode], cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def transpose(self,startVertex):
        g = Graph()
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                g.addEdge(nextVertex, startVertex)
                nextVertex.setColor('gray')
            self.transpose(nextVertex)
        startVertex.setColor('black')
        return g

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
    
    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time+=1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time+=1
        startVertex.setFinish(self.time)
  
  
    def topologicalSortHelper(self, startVertex, stack):
        startVertex.setColor('gray')
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.topologicalSortHelper(nextVertex, stack)
        stack.insert(0, startVertex)
    
    def topologicalSort(self):
        s = Stack.Stack()
        for i in range(self.getConnections()):
            if self.getColor() == 'white':
                self.topologicalSortHelper(i, s)
        print(s)        
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wFile:
        word =  line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1])
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2), (-1,2), (-2,-1), (-2,1), (1, -2), (1,2), (2,-1), (2,1)]
    
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False



def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(orderByAvail())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1,path, nbrList[i], limit)
            i+=1
        
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0 #number of connections for reach neighbor
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c+=1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]
        
            
g = Graph()
for i in range(6):
    g.addVertex(i)

#print(g.vertList)
g.addEdge(5,2,5)
g.addEdge(5,0,2)
g.addEdge(4,0,4)
g.addEdge(4,1,9)
g.addEdge(2,3,7)
g.addEdge(3,1,3)
traverse(g.vertList[1])
traverse(g.transpose(g.vertList[0]))
#g.addEdge(4,0,1)
#g.addEdge(5,4,8)
#g.addEdge(5,2,1)
#for v in g:
#    for w in v.getConnections():
#        print("( %s, %s )" % (v.getId(), w.getId()))
        

    