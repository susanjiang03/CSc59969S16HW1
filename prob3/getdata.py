#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

items = ['pigs','ducks','goats','sheep','cattle','chickens','turkeys']
continents = ['Africa +', 'Northern America +', 'South America +', 'Asia +', 'Europe +', 'Australia and New Zealand +']

#extra data
def getdata():
  dict = {}
  for item in items:
    filename = item + ".csv"
    with open( filename,'rU') as f:
      reader = csv.reader(f)
      data = list(reader)
      header = data[0]
      #find index of needed columns
      i = header.index('Country or Area')
      y = header.index('Year')
      u = header.index('Unit')
      v = header.index('Value')
      M = max(i,u,v)

      #find the item unit and value of each continent, and append to a dictionary
    for c in continents:
      for row in data[1:]:
        if len(row) < M:
            continue
        else:
            if c == row[i] and row[y] == '2007':
                value = int(float(row[v]))
                if row[u]== '1000 Head':
                   value = value*1000
                if c in dict.keys():
                   dict[c].append(value)
                else:
                   dict[c]=[value]

  return dict