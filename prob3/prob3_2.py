#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
from getdata import getdata

items = ['pigs','ducks','goats','sheep','cattle','chickens','turkeys']
continents = ['Africa +', 'Northern America +', 'South America +', 'Asia +', 'Europe +', 'Australia and New Zealand +']


#Now, try to find a way to combine these in a single graph. How will you show continent vs. animal?

pigs = []
ducks = []
goats = []
cattle = []
chickens =[]
turkeys =[]

dict = getdata()

for con in continents:
    pigs.append(dict[con][0])
    ducks.append(dict[con][1])
    goats.append(dict[con][2])
    cattle.append(dict[con][3])
    chickens.append(dict[con][4])
    turkeys.append(dict[con][5])

 #set the position and width for the bars
N = len(continents)
pos = list(range(N))
bar_width = 0.15

#plotting the bars
fig, ax = plt.subplots()

bar1 = plt.bar(pos, pigs, bar_width, alpha =0.5,color ='black')
bar2 = plt.bar([p + bar_width for p in pos], ducks, bar_width, alpha =0.5, color ='red')
bar3 = plt.bar([p + bar_width*2 for p in pos], goats, bar_width, alpha =0.5,color ='yellow')
bar4 = plt.bar([p + bar_width*3 for p in pos], cattle, bar_width, alpha =0.5,color ='blue')
bar5 = plt.bar([p + bar_width*4 for p in pos], chickens, bar_width, alpha =0.5, color = 'green')
bar6 =plt.bar([p + bar_width*5 for p in pos], turkeys, bar_width, alpha =0.5, color = 'purple')

ax.set_ylabel('Head')
ax.set_xlabel('Continents')
ax.set_title("Compares the numbers of 7 animals in 6 continents")
ax.set_xticks([p + 4 * bar_width for p in pos])
ax.set_xticklabels(items)

# Setting the x-axis and y-axis limits
plt.ylim([0,max(pigs + ducks + goats + cattle + chickens + turkeys)])

plt.legend(continents,loc='upper left')
plt.grid()
plt.show()
