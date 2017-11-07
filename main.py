#!/usr/bin/env python
from misc import readInput,avBucketCreator
from programma import User,Programma
import Queue
import argparse

def printAvs(availabilities):
	for av in availabilities:
		stri = ""
		for usr in av:
			stri += usr + " "
		print "[",stri,"]"

def isSolution(prog):
    print("ENTERING IS SOLUTION")
    for v in prog:
        if v == None:
            print("This IS NOT A SOLLUTION")
            return False;
    print("THIS IS A SOLUTION")
    return True;
        # if a vardia (not vardia1) is None False

def dfs(q):
    solutionFound = False
    while not q.empty() :
        root = q.get()
        print "Just Poped: "
        root.printProg()
        for usr_name,usr in root.getUsersDict().iteritems():
            print (usr_name," has hours ",usr.getAvHours())
        if isSolution(root.getProg()):
            solutionFound = True
            break
        print "             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print
        children =  root.getChildren(availabilities)
        print("             ++++++++PRINTING CHILDREN[",len(children),"]++++++++++++++++")
        for c in children:
            print("++--==PUSHING CHILD==--++")
            c.printProg()
            printAvs(availabilities)
            q.put(c)

    return solutionFound


ap = argparse.ArgumentParser()
ap.add_argument("-i","--input",required = True)


args = vars(ap.parse_args())
inputPath = args["input"]

availabilities = readInput(inputPath)
printAvs(availabilities)


q = Queue.LifoQueue()
root =  Programma()
root.printProg()
q.put(root)
solutionFound = dfs(q)

if not(solutionFound):
    #ksekina apo paraskeyi na min vazeis vardia 2
    backup = list(availabilities)
    availabilities[13] = ["nobody"]
    q = Queue.LifoQueue()
    root =  Programma()
    root.printProg()
    q.put(root)
    solutionFound = dfs(q)




