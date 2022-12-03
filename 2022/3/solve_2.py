#!/usr/bin/env python3
import string
data = open('input.txt', 'r').read().splitlines()

priority = ' ' + string.ascii_lowercase + string.ascii_uppercase
sum = 0

data_grouped = []
cur_group = []

for line in data:
  cur_group.append(line)

  if len(cur_group) == 3:
    data_grouped.append(cur_group)
    cur_group = []


for line in data_grouped:
  comp_1, comp_2, comp_3 = line
  we_done = False

  for i in range(len(comp_1)):
    for j in range(len(comp_2)):
      for k in range(len(comp_3)):
        if comp_1[i] == comp_2[j] == comp_3[k]:

          pr = priority.index(comp_1[i])
          sum += pr
          we_done = True
          break 

      if we_done:
        break
    
    if we_done:
      break

print(sum)
  
