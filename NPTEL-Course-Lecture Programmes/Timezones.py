# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:57:49 2021

@author: Lakhan Kumawat


from datetime import datetime as dt
import pytz
print(dt.now()) 


tz=pytz.timezone('Asia/Bangkok')

print(dt.now(tz))
"""

import calendar
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

find=input().split()
lis=list(find)
try:
    dayNumber = calendar.weekday(int(lis[2]), int(lis[0]),int(lis[1])) 
    print(days[dayNumber])
except Exception as e:
    
    print(e)
    
