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
