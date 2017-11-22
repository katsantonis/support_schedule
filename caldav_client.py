#!/usr/bin/env python3
import caldav
from datetime import datetime,date,time
import datetime
from config import calendar_urls,users,owncloud_url,vardies,default_events
import getpass



def add_availability_string_to_availabilities(availability_string,day,availabilities):
    user = ""
    vardia = ""
    for u in users:
        if u in availability_string:
            user = u

    # if saturday
    if day == 5:
        availabilities[15].append(user)
    #if sunday
    elif day == 6:
        availabilities[16].append(user)
    #if weekday
    else:
        for v in vardies:
            if v in availability_string:
                availabilities[3*day + int(v) - 1].append(user)

    return availabilities




def caldav_date_to_weekday(caldav_date):
    year  = int(caldav_date[0:4])
    month = int(caldav_date[4:6])
    day   = int(caldav_date[6:8])
    return date(year,month,day).weekday()

#TODO ENDTIME is also importan in case 
#a user declares his availability with the same event 
#that for rxample starts on Monday and Ends on Wednesday
def parse_caldav_event(event):
    result = []
    lines = event.splitlines()
    for line in lines:
        if "DTSTART" in line:
            start_day = caldav_date_to_weekday(line.split(":")[1])
        elif "DTEND" in line:
            end_day   = caldav_date_to_weekday(line.split(":")[1]) 
        elif "SUMMARY" in line:
            availability_string = line.split(":")
            availability_string = " ".join(availability_string[1:])

    for day in range(start_day,end_day):
        result.append((day,availability_string))
    
    return result
    
def get_next_week_dates():
    #returns next weeks monday and sunday
    today              = date.today()
    today_as_weekday   = today.weekday()
    next_monday        = today + datetime.timedelta(days=7-today_as_weekday)
    next_sunday        = next_monday + datetime.timedelta(days=6)
    return next_monday,next_sunday


def fetch_availabilities(username,password):
    availabilities = []
    users_no_availability = []
    for i in range(17):
        availabilities.append([])
    
    client = caldav.DAVClient(owncloud_url,username = username , password = password)
    principal = client.principal()
    next_monday,next_sunday = get_next_week_dates()
    for u in users:
        user_availability_events = []
        use_default_events = False
        if u in calendar_urls:
            user_availability_calendar            = principal.calendar(client,calendar_urls[u])
            user_availability_events = user_availability_calendar.date_search(next_monday,next_sunday) 

        print("checking user {}".format(u))
        if not user_availability_events:
            print("No calendar availabilities for user [{}]".format(u))
            user_availability_events = default_events[u]
            use_default_events = True
        if not user_availability_events:
            print ("No default availabilities for user [{}]".format(u))
        for event in user_availability_events:
            if use_default_events:
                day,availability_string = event
                data = [(day,availability_string)]
            else:
                #data = [(day,availability_string),(day,availability_string)]
                data = parse_caldav_event(event.data)
                print("day = {}".format(day))
                print("availability_string = {}".format(availability_string))
                for day,availability_string in data:
                    availabilities = add_availability_string_to_availabilities(availability_string,day,availabilities)

    return availabilities


