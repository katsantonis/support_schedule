#!/usr/bin/env python3
import caldav
from datetime import datetime,date,time
import datetime
import getpass
from calendar import monthrange
from config import owncloud_url,users
from user_timesheet import WorkDayList,WorkDay,UserTimesheet

def parse_summary_string(line,workday):
words  =  line.split()
vardies_cp = list(vardies)
vardies_rev_iter = iter(vardies.reverse())
for i in range(len(words),0,-1):
    for u in users:
        if u in words[i]:
            workday.add(vardies_rev_iter.next(),u)    
   

def parse_date_string(date_string):
    year  = date_string[0:4]
    month = date_string[4:6]
    day   = date_string[6:]
    return datetime.date(int(year),int(month),int(day))

def parse_events(events):
    day_list = WorkDayList()
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

        for x in range(start_date.day,end_date.day):
            offset          = x - start_date.day
            current_date    = start_date + datetime.timedelta(days=offset)
            current_workday =  WorkDay(current_date)
            parse_summary_string(line,current_workday)
            day_list.append_day(current_workday)
        
        day_list.print_list()


    

def main():
    username = input("username:")
    password = getpass.getpass()
    current_year = date.today().year

    months_string = input("Enter months separated by space: ")
    months = months_string.split()

    client    = caldav.DAVClient(owncloud_url,username = username , password = password)
    principal = client.principal()

    support_vardies = principal.calendar(client,support_vardies)

for month in months:
    first_month_day,last_month_day = monthrange(current_year,int(month))
    start_day = datetime.date(current_year,int(month),first_month_day)
    end_day   = datetime.date(current_year,int(month),last_month_day)

    events = support_vardies.date_search(start_day,end_day)
    parse_events(event)



if __name__ == "__main__":
    import os, sys 
    parentPath = os.path.abspath("..")
    if parentPath not in sys.path:
        sys.path.insert(0, parentPath)
    
    main()
