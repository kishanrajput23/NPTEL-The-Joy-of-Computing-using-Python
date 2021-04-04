# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"Hello World"
""""For Calculating The Mean"""
from statistics import mean
Estimates = [1000,1900,2000,1500]
Estimates.sort()
tv = int(0.1*len(Estimates))
Estimates = Estimates[tv:len(Estimates)-tv]
print(mean(Estimates))

"""For drawing a graph in python"""
import matplotlib.pyplot as plt
plt.plot([1,3,4,9],[9,11,13,25],'r--')
plt.ylabel("Y-axis")
plt.xlabel("X-axis")

