#!/usr/bin/env python
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from config import days,weekend,users,vardies,days2Nums


def slot_to_day_vardia(slot):
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
        day = days[int(slot/3)]
    return(day,vardia)



def read_input(filename):
    availabilities = []
    for i in range(17):
        availabilities.append( [] )	
    current_user   = ""
    current_day    = ""
    current_vardia = 0

    with open(filename) as f:

        for line in f:
            l = line.strip()
            if l in days:
                current_day = l
            else:
                words = l.split()
                for word in words:
                    if word in users :
                        current_user = word
                        if current_day == "Saturday":
                            availabilities[15].append(current_user)
                        elif current_day == "Sunday":
                            availabilities[16].append(current_user)
                    if word in vardies:
                        vardia = int(word)
                        availabilities[3*days2Nums[current_day]+vardia -1 ].append( current_user )

        return availabilities



		
		

