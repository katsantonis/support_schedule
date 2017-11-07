#!/usr/bin/env python
import hashlib
import sys
from config import days,weekend,days2Nums,users

def slotToDayVardia(slot):


	day = ""
	vardia = -1
	if slot == 16:
		day = "Sunday"
		vardia = 2
	elif slot == 15:
		day = "Saturday"
		vardia = 2
	else:
		vardia = slot % 3 +1
		day = days[slot/3]
	return(day,vardia)

def worksAtThatDay(usr_name,prog,day):


	if day == "Saturday":
		return prog[15] == usr_name
	elif day =="Sunday":
		return prog[16] == usr_name
	else:
		dayNum = days2Nums[day]
		for i in range(3):
			if prog[3*dayNum+i] == usr_name:
				return True
		return False

class User:
	
	def __init__(self,name,av_hours = 20):


		self.name     = name
		self.avHours = av_hours
	
	def printUser(self):


		print "Name: "    ,self.name
		print "Av.hours: ",self.av_hours
	
	def getName(self):


		return self.name
	
	def getAvHours(self):


		return self.avHours

	def setAvHours(self,avHours):


		self.avHours = avHours
	
	def addHoursOfVardia(self,vardia):


		if vardia != 1:
			self.avHours += 8
		else:
			self.avHours +=4

	def removeHoursOfVardia(self,vardia):


		if vardia != 1:
			self.avHours -= 8
		else:
			self.avHours -= 4

	def getCopy(self):


		c = User(self.getName(),av_hours = self.getAvHours())
		return c

	def canWorkVardia(self,vardia):


		print("NAME: ",self.getName(),"has av hours: ",self.getAvHours(),"checking vardia: ",vardia,type(vardia))
		if vardia == 1 and self.getAvHours() >= 4 :
			return True
		elif self.getAvHours() < 8 :
			return False
		else:
			return True
	

class Programma:
	
	def __init__(self):


            self.usersDict = {"hadem":User("hadem",24),"mikem":User("mikem"),"konnos":User("konnos"),"jstam":User("jstam"),"canagnostou":User("canagnostou"),"sdelis":User("sdelis",24),"orespan":User("orespan",24),"nobody":User("nobody",16)}

            self.prog = []
	    for i in range(17):
	    	self.prog.append(None)
	
	def myHash(self):
		for x in prog:
			total += x
			
		return hashlib.md5(total.encode()).hexdigest()

	def getUsersDict(self):
		return self.usersDict

	def getVadia(self,day,vardia):
		if day not in weekend:
			index = 3*days2Nums[day] + vardia -1
		if day == "Saturday":
			index = 15
		if day== "Sunday":
			index = 16

		return prog[index]
	
	def setVardia(self,day,vardia,usr_name):
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
			self.getUsersDict()[prev_usr_name].addHoursOfVardia(vardia)
			
		self.prog[index] = curr_usr_name
		self.getUsersDict()[curr_usr_name].removeHoursOfVardia(vardia)
	
	def getProg(self):
		return self.prog
	
	def setProg(self,prog):
		for i in range(len(prog)):
			self.prog[i] = prog[i]
		
	

	def printProg(self):
		for day in days:
			print "==",day,"=="
			if day == "Saturday":
				print self.prog[15]
			elif day == "Sunday":
				print self.prog[16]
			else:
				for i in range(3):
					print i+1,".",self.prog[3*days2Nums[day]+ i]

	def copyOfUserDict(self):
		newUserDict = {}
		for u in users:
			newUserDict[u] = self.usersDict[u].getCopy()
		
		return newUserDict

	def setNewUsersDict(self,ud):
		self.usersDict = ud

	def getCopy(self):
		c = Programma()
		c.setProg( self.getProg() )
		c.setNewUsersDict(self.copyOfUserDict())
		return c

		
				
	def getChildren(self,availabilities):
		children = []
		for slot in range(17):
			print(self.prog[slot]==None)
			if self.prog[slot] == None:
				break
		
		print("checking slot: ",slot)
		avs = availabilities[slot]
		print("avs of this slot: ",avs)
		day,vardia = slotToDayVardia(slot)
		for usr_name in avs:
			child = self.getCopy();
			if child.getUsersDict()[usr_name].canWorkVardia(vardia) and not worksAtThatDay(usr_name,child.getProg(),day) :
				child.setVardia(day,vardia,usr_name)
				children.append(child)

		return children
		










	
