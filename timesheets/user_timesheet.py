import datetime


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
    

class WorkDay():
    def __init__(self,day):
        self.day = day
        self.vardies = ["1":"nobody","2":"nobody","3":"nobody"]

    def add(vardia,user):
        self.vardies[vardia] = user

    def print_out(self):
        print("==",self.day.day,"-",self.day.month,"-",self.day.year,"==")
        for vardia,user in self.vardies.items():
            print(vardia,". ",user)



class UserTimsheet():
    
    def __init__(self,name):
        self.name = name
        self.timesheet = []

    def get_name(self):
        return self.name

    def get_timesheet(self):
        return self.timesheet()

    def add(self,day,vardia)
        if vardia=="2" or vardia=="3":
            hours = 8
        elif vardia=="1"
            hours = 4
        else
            hours = -1

        self.timesheet.append((day,vardia,hours))

    def get_total_hours(self):
        total_hours=0
        for t in self.timesheet:
            total_hours += t[2]
        return total_hours

