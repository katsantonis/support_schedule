#!/usr/bin/env python3
from misc import read_input
from programma import User,Programma
import queue
import argparse
from caldav_client import fetch_availabilities
import getpass

def print_avs(availabilities):
    for av in availabilities:
        stri = ""
        for usr in av:
            stri += usr + " "
        print("[{}]".format(stri))

def is_solution(prog):
 #   print("ENTERING IS SOLUTION")
    for v in prog:
        if v == None:
   #         print("This IS NOT A SOLLUTION")
            return False;
  #  print("THIS IS A SOLUTION")
    return True;
     # if a vardia (not vardia1) is None False

def dfs(q,availabilities):
    solution_found = False
    solutions = []
    while not q.empty() :
        root = q.get()
    #    print("Just Poped: ")
     #   root.print_prog()
     #   for usr_name,usr in root.get_users_dict().items():
     #       print ("{} has hours {}".format(usr_name,usr.get_av_hours()))
        if is_solution(root.get_prog()):
            solutions.append((root,root.get_score()))
           # if len(solutions) > 20000:
           #     break
      #  print("             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
     #   print()
        children =  root.get_children(availabilities)
     #   print("             ++++++++PRINTING CHILDREN[",len(children),"]++++++++++++++++")
        for c in children:
     #       print("++--==PUSHING CHILD==--++")
      #      c.print_prog()
       #     print_avs(availabilities)
            q.put(c)

    return solutions

#TODO function tha decides how many solutions to print
def print_solutions(solutions):
    if solutions == []:
        print("No Solutions Found")
    else:
        best_score = solutions[-1][1]
    for i in range(len(solutions)-1,0,-1):
        if solutions[i][1] == best_score:
            print("++++++++++++++++++++++++++")
            print(solutions[i][0].print_prog())
            print(solutions[i][1])
            print("++++++++++++++++++++++++++")
    

def main():
    username = input("username:")
    password = getpass.getpass()
            
    availabilities = fetch_availabilities(username,password)
    if not availabilities:
        print("Exiting ...")
        exit()
    print_avs(availabilities)


    q = queue.LifoQueue()
    root =  Programma()
    root.print_prog()
    q.put(root)
    solutions = dfs(q,availabilities)
    
    #sort by score
    solutions = sorted(solutions, key = lambda x: x[1])
    
    print("Print Solutions")
    print_solutions(solutions)
    

if __name__ == "__main__":
    import os, sys 
    parentPath = os.path.abspath("..")
    if parentPath not in sys.path:
        sys.path.insert(0, parentPath)

     main()


