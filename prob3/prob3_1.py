#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from getdata import getdata

items = ['pigs','ducks','goats','sheep','cattle','chickens','turkeys']
continents = ['Africa +', 'Northern America +', 'South America +', 'Asia +', 'Europe +', 'Australia and New Zealand +']

# Make a separate bar graph for each of the continents comparing the number of pigs, ducks, goats, sheep, cattle, chickents and turkeys.

def prob3_1():
  dict = getdata()
  fig = plt.figure()
#plot in 3*2
  i = 321
  fig = plt.figure()

  N = len(items)
  for d in dict.keys():
     item_value = dict[d]
     ind = np.arange(N)    # the x locations for the groups
     plt.subplot(i)
     i = i + 1
     p = plt.bar(ind, item_value, align = 'center',width=1.0,)
     #set colors
     colors = ['pink','yellow','blue','green','wheat','red','orange']
     for x in range(N):
        p[x].set_color(colors[x])

     plt.ylabel('Head')
     plt.title(d)
     plt.xticks(ind, items)

  plt.show()



prob3_1()

