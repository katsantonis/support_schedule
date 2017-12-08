#!/usr/bin/env python3
import caldav
from datetime import datetime,date,time
import datetime
import getpass
from calendar import monthrange

users=["sdelis","konnos","mikem","orespan","hadem","canagnostou"]
work_days = []
global users
global work_days

def parse_summary_string(line,workday):
    

def parse_date_string(date_string):
    year  = date_string[0:4]
    month = date_string[4:6]
    day   = date_string[6:]
    return datetime.date(int(year),int(month),int(day))

def parse_event(event):
    data = event.data
    lines = data.splitlines()
    for line in lines:
        if "DTSTART" in line:
            start_date = parse_date_string(line.split(":")[-1])
        if "DTEND"   in line:
            end_date = parse_date_string(line.split(":")[-1])        
        if "SUMMARY" in line:
            parse_summary_string(line)

        for x in range(start_date.day,end_date.day):
            offset          = x - start_date.day
            current_date    = start_date + datetime.timedelta(days=offset)
            current_workday =  WorkDay(current_date)
            parse_summary_string(line,WorkDay) ##STOPED HERE

    


username = input("username:")
password = getpass.getpass()
current_year = date.today().year

print(type(password))
months_string = input("Enter months separated by space: ")
months = months_string.split()


owncloud_url    = "https://colab.noc.grnet.gr/remote.php/dav/calendars/"
calendar_url = "https://colab.noc.grnet.gr/remote.php/dav/calendars/b38d8d60-c5c0-1036-8ecb-11b6346f5763/%ce%92%ce%ac%cf%81%ce%b4%ce%b9%ce%b5%cf%82support_shared_by_6fb185e4-c0ca-1034-9776-a916203cc14b/"

client    = caldav.DAVClient(owncloud_url,username = username , password = password)
principal = client.principal()

support_vardies = principal.calendar(client,calendar_url)

for month in months:
    first_month_day,last_month_day = monthrange(current_year,int(month))
    start_day = datetime.date(current_year,int(month),first_month_day)
    end_day   = datetime.date(current_year,int(month),last_month_day)

    events = support_vardies.date_search(start_day,end_day)
    for event in events:
        parse_event(event)
