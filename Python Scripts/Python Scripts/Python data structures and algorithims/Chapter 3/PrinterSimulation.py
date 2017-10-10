# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:55:48 2017

@author: Nathan
"""
from Queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None
            
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self, new_task):
        self.currentTask = new_task
        self.timeRemaining = new_task.getPages() * 60/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currtime):
        return currtime - self.timestamp

def simulation(numsec, ppm):
    
    printer = Printer(ppm)
    printqueue = Queue()
    taskwaittime = []
    
    for currsec in range(numsec):
        
        if newtask():
            task = Task(currsec)
            printqueue.enqueue(task)
        
        if (not printer.busy()) and (not printqueue.isEmpty()):
            nextTask = printqueue.dequeue()
            taskwaittime.append(nextTask.waitTime(currsec))
            printer.startNext(nextTask)
        
        printer.tick()
    
    averageofWaitTimes = sum(taskwaittime)/len(taskwaittime)
    print("Average Wait %6.2f secs %4d tasks remaining." \
              %(averageofWaitTimes, printqueue.size()))



def newtask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
    
for i in range(10):
    simulation(3600, 10)