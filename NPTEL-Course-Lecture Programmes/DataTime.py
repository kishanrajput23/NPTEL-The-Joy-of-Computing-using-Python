# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:43:28 2021

@author: Lakhan Kumawat
"""
import datetime
dateToday=datetime.datetime.now()
print(dateToday)
dateToday=datetime.date.today().strftime("%Y")
print(dateToday) #prints the year
dateToday=datetime.date.today().strftime("%B")
print(dateToday) #prints the month
dateToday=datetime.date.today().strftime("%d")
print(dateToday) #prints the date
dateToday=datetime.date.today().strftime("%W")
print(dateToday) #prints the week number of year
dateToday=datetime.date.today().strftime("%w")
print(dateToday) #prints the week number of month
dateToday=datetime.date.today().strftime("%j")
print(dateToday) #prints the day number of year
dateToday=datetime.date.today().strftime("%A")
print(dateToday) #prints the day