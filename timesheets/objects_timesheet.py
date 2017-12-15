import datetime
import sys
sys.path.append('..')
from config import users

class WorkDayList():
    def __init__(self):
        self.list = []
    
    def get_list(self):
        return self.list
    
    def append_day(self,day):
        self.list.append(day)    

    def print_list(self):
        for work_day in self.list:
            work_day.print_out()
    
    def sort_me(self):
        self.list = sorted(self.list, key = lambda work_d: work_d.day.day ) 

class WorkDay():
    def __init__(self,day):
        self.day = day
        self.vardies = {"1":"nobody","2":"nobody","3":"nobody"}

    def add(self,vardia,user):
        self.vardies[vardia] = user

    def print_out(self):
        print("==",self.day.day,"-",self.day.month,"-",self.day.year,"==")
        for vardia,user in self.vardies.items():
            print(vardia,". ",user)

    def get_vardies(self):
        return self.vardies

    def get_day(self):
        return self.day


class Timesheets():
    
    def __init__(self,work_day_list):
        self.dict = {}

        for user in users:
            self.dict[user] = UserTimesheet(user)

        for w_d in work_day_list.get_list():
            self.add_work_day(w_d)


    def get_users(user):
        return self.dict[user]
    
    def add_work_day(self,w_d):
        vardies = w_d.get_vardies()
        day     = w_d.get_day()
        for vardia,user in vardies.items():
            self.dict[user].add(day,vardia)

    def print_users_ts(self,user):
        self.dict[user].print_timesheet(user)
    

class UserTimesheet():
    
    def __init__(self,name):
        self.name = name
        self.timesheet = []

    def get_name(self):
        return self.name

    def get_timesheet(self):
        return self.timesheet()

    def add(self,day,vardia):
        if vardia=="2" or vardia=="3":
            hours = 8
        elif vardia=="1":
            hours = 4
        else:
            hours = -1

        self.timesheet.append((day,vardia,hours))

    def get_total_hours(self):
        total_hours=0
        for t in self.timesheet:
            total_hours += t[2]
        return total_hours

    def print_timesheet(self,user):
        print("===",user,"===")
        for x in self.timesheet:
            day    = x[0]
            vardia = x[1]
            hours  = x[2]
            print(day.day,"/",day.month,"/",day.year," ",vardia," ",hours)
        
        print("total:",self.get_total_hours())

