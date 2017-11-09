#!/usr/bin/env python
from misc import read_input
from programma import User,Programma
import Queue
import argparse

def print_avs(availabilities):
    for av in availabilities:
        stri = ""
	for usr in av:
	    stri += usr + " "
	print "[",stri,"]"

def is_solution(prog):
    print("ENTERING IS SOLUTION")
    for v in prog:
        if v == None:
            print("This IS NOT A SOLLUTION")
            return False;
    print("THIS IS A SOLUTION")
    return True;
     # if a vardia (not vardia1) is None False

def dfs(q,availabilities):
    solution_found = False
    solutions = []
    while not q.empty() :
        root = q.get()
        print "Just Poped: "
        root.print_prog()
        for usr_name,usr in root.get_users_dict().iteritems():
            print (usr_name," has hours ",usr.get_av_hours())
        if is_solution(root.get_prog()):
            solutions.append((root,root.get_score()))
            if len(solutions) > 100:
                break
        print "             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print
        children =  root.get_children(availabilities)
        print("             ++++++++PRINTING CHILDREN[",len(children),"]++++++++++++++++")
        for c in children:
            print("++--==PUSHING CHILD==--++")
            c.print_prog()
            print_avs(availabilities)
            q.put(c)

    return solutions

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--input",required = True)


    args = vars(ap.parse_args())
    input_path = args["input"]

    availabilities = read_input(input_path)
    print_avs(availabilities)


    q = Queue.LifoQueue()
    root =  Programma()
    root.print_prog()
    q.put(root)
    solutions = dfs(q,availabilities)
    
    #sort by score
    solutions = sorted(solutions, key = lambda x: x[1])

    for sol in solutions:
        print("++++++++++++++++++++++++++")
        print(sol[0].print_prog())
        print(sol[1])
        print("++++++++++++++++++++++++++")

    
    #if not(solution_found):
    #    #ksekina apo paraskeyi na min vazeis vardia 2
    #   backup = list(availabilities)
    #    availabilities[13] = ["nobody"]
    #    q = Queue.LifoQueue()
    #    root =  Programma()
    #    root.print_prog()
    #    q.put(root)
    #    solution_found = dfs(q,availabilities)

if __name__ == "__main__":
     main()
    #p = Programma()
    #p.prog = ["konnos","","hadem","hadem","konnos","orespan","hadem","","sdelis","sdelis","","orespan","sdelis","","konnos","konnos",""]
    #p.print_prog()
    #print(p.count_3_1())
    #print(p.count_double_vardia_1())
    #print(p.get_score())


