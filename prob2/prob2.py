#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
data ={}
with open ('goats_UNdata.csv','rU') as f:
     reader = csv.reader(f)
     data = list(reader)

#get year
Year = data[0][1:]
#loop through data, plot each line for each continent
for row in data[1:]:
    plt.plot(Year,row[1:],label=row[0],linewidth = 2.0)

plt.legend(loc='upper left')
x = range(1961,2008)
plt.xticks(x, Year, rotation= 45 )
plt.xlabel('Year\n Data Source: http://data.un.org/Explorer.aspx?d=FAO&f=itemCode%3a1079')
plt.ylabel('The population of goats (head)')
plt.title('The population of the goats in the continents\n Africa, North America, South America, Asia, Europe and Austrailia + New Zeland')
plt.grid(True)
plt.show()
