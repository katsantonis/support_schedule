#!/usr/bin/env python
import hashlib
import sys
from config import days,weekend,days2Nums,users
from misc import slot_to_day_vardia

class User:
	
    def __init__(self,name,av_hours = 20):
	self.name     = name
	self.av_hours = av_hours
	
    def print_user(self):
	print "Name: "    ,self.name
	print "Av.hours: ",self.av_hours
	
    def get_name(self):
	return self.name
	
    def get_av_hours(self):
	return self.av_hours

    def set_av_hours(self,avHours):
	self.avHours = av_hours
	
    def add_hours_of_vardia(self,vardia):
	if vardia != 1:
	    self.av_hours += 8
	else:
	    self.av_hours +=4

    def remove_hours_of_vardia(self,vardia):
        if vardia != 1:
	    self.av_hours -= 8
	else:
	    self.av_hours -= 4

    def get_copy(self):
	c = User(self.get_name(),av_hours = self.get_av_hours())
	return c


    def can_work_vardia(self,vardia):
	print("NAME: ",self.get_name(),"has av hours: ",self.get_av_hours(),"checking vardia: ",vardia,type(vardia))
	if vardia == 1 and self.get_av_hours() >= 4 :
	    return True
	elif self.get_av_hours() < 8 :
	    return False
	else:
	    return True

    def works_that_day(self,prog,day):
        if day == "Saturday":
            return prog[15] == self.get_name()
        elif day =="Sunday":
            return prog[16] == self.get_name()
        else:
            dayNum = days2Nums[day]
            for i in range(3):
                if prog[3*dayNum+i] == self.get_name():
	            return True
	    return False


	

class Programma:
	
    def __init__(self):
        self.users_dict = {"hadem":User("hadem",24),"mikem":User("mikem"),"konnos":User("konnos"),"jstam":User("jstam"),"canagnostou":User("canagnostou"),"sdelis":User("sdelis",24),"orespan":User("orespan",24),"nobody":User("nobody",16)}

        self.prog = []
	for i in range(17):
	    self.prog.append(None)
	
    def my_hash(self):
        for x in prog:
	    total += x		
	return hashlib.md5(total.encode()).hexdigest()

    def get_users_dict(self):
	return self.users_dict

    def get_vadia(self,day,vardia):
	if day not in weekend:
	    index = 3*days2Nums[day] + vardia -1
	if day == "Saturday":
	    index = 15
	if day== "Sunday":
	    index = 16

	return prog[index]
	
    def set_vardia(self,day,vardia,usr_name):
	if day not in weekend:
	    index = 3*days2Nums[day] + vardia -1
	    print "index = ",index
	elif day == "Saturday":
	    index = 15
	elif day == "Sunday":
	    index = 16

	prev_usr_name = self.prog[index]
	curr_usr_name = usr_name

	if prev_usr_name != None :
	    self.getUsersDict()[prev_usr_name].add_hours_of_vardia(vardia)
			
	self.prog[index] = curr_usr_name
	self.get_users_dict()[curr_usr_name].remove_hours_of_vardia(vardia)
	
    def get_prog(self):
	return self.prog
	
    def set_prog(self,prog):
	for i in range(len(prog)):
	    self.prog[i] = prog[i]
		
	

    def print_prog(self):
	for day in days:
	    print "==",day,"=="
	    if day == "Saturday":
	        print self.prog[15]
	    elif day == "Sunday":
		print self.prog[16]
	    else:
	        for i in range(3):
		    print i+1,".",self.prog[3*days2Nums[day]+ i]

    def copy_of_user_dict(self):
        new_user_dict = {}
	for u in users:
	    new_user_dict[u] = self.users_dict[u].get_copy()
	
	return new_user_dict

    def set_new_users_dict(self,ud):
	self.users_dict = ud

    def get_copy(self):
	c = Programma()
	c.set_prog( self.get_prog() )
	c.set_new_users_dict(self.copy_of_user_dict())
	return c

		
				
    def get_children(self,availabilities):
	children_progs = []
	for slot in range(17):
	    print(self.prog[slot]==None)
	    if self.prog[slot] == None:
	        break
		
	print("checking slot: ",slot)
	avs = availabilities[slot]
	print("avs of this slot: ",avs)
	day,vardia = slot_to_day_vardia(slot)
	for usr_name in avs:
	    child = self.get_copy();
            user = child.get_users_dict()[usr_name]
	    if user.can_work_vardia(vardia) and not user.works_that_day(child.get_prog(),day):
	        child.set_vardia(day,vardia,usr_name)
		children_progs.append(child)

	return children_progs
    
    def count_3_1(self):
        counter_3_1 = 0
        prog = self.get_prog()
        #for every vardia 3
        for v in range(2,len(prog),3):
            #if vardia_3  == next_day_vardia_1
            if prog[v] == prog[v+1]:
                counter_3_1 += 1
        return counter_3_1

    def count_double_vardia_1(self):
        counter = 0
        prog  = self.get_prog()
        for name,user in self.get_users_dict().items():
            user_name = user.get_name()
            users_vardia_1_counter = 0
            for v1 in range(0,13,3):
                if prog[v1]==user_name:
                    users_vardia_1_counter+=1

            if users_vardia_1_counter >= 2:
                counter += users_vardia_1_counter-1

        return counter

    def same_user_weekend(self):
        prog = self.get_prog()
        if prog[15] == prog[16]:
            return 1
        else:
            return 0
            

    def get_score(self):
        negative_points = (0.1 + self.count_3_1() + self.count_double_vardia_1() + self.same_user_weekend())
        score = 1.0/negative_points
        return score

		










	
