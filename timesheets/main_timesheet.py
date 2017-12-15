#!/usr/bin/env python3
import caldav
from datetime import datetime,date,time
import datetime
import getpass
from calendar import monthrange
from objects_timesheet import WorkDayList,WorkDay,Timesheets,UserTimesheet

def parse_summary_string(line,workday):
    words  =  line.split(" ")
    vardies_cp = list(vardies)
    vardies.reverse()
    vardies_rev_iter = iter(list(vardies))
    vardies.reverse()
    for w in reversed(words):
        for u in users:
            if u in w:
                print ("user: ",u)
                workday.add(next(vardies_rev_iter),u)    
   

def parse_date_string(date_string):
    year  = date_string[0:4]
    month = date_string[4:6]
    day   = date_string[6:]
    return datetime.date(int(year),int(month),int(day))

def parse_events(events):
    day_list = WorkDayList()
    start_date = ""
    end_date = ""
    summary = ""
    for event in events:
        data = event.data
        lines = data.splitlines()
        for line in lines:
            if "DTSTART" in line:
                start_date = parse_date_string(line.split(":")[-1])
            if "DTEND"   in line:
                end_date = parse_date_string(line.split(":")[-1])        
            if "SUMMARY" in line:
                summary = line
        print("start: ",start_date,"end: ",end_date,"summary: ",summary)

        for x in range(0,(end_date - start_date).days):
            current_date    = start_date + datetime.timedelta(x)
            current_workday =  WorkDay(current_date)
            parse_summary_string(summary,current_workday)
            day_list.append_day(current_workday)
    
    day_list.sort_me()   
    day_list.print_list()
    return day_list
    
    

    

def main():
    username = input("username:")
    password = getpass.getpass()
    current_year = date.today().year

    months_string = input("Enter months separated by space: ")
    months = months_string.split()

    client    = caldav.DAVClient(owncloud_url,username = username , password = password)
    principal = client.principal()

    support_vardies_cal = principal.calendar(client,support_vardies)

    for month in months:
        first_month_day,month_duration = monthrange(current_year,int(month))
        start_day = datetime.date(current_year,int(month),1)
        end_day   = start_day + datetime.timedelta(month_duration)   
        
             

    events = support_vardies_cal.date_search(start_day,end_day)
    
    day_list   = parse_events(events)
    timesheets = Timesheets(day_list)
    while True:
        user = input("Type User: ")
        timesheets.print_users_ts(user)


if __name__ == "__main__":
    import os, sys 
    parentPath = os.path.abspath("..")
    if parentPath not in sys.path:
        sys.path.insert(0, parentPath)
    from config import owncloud_url,users,support_vardies,vardies
    
    main()
