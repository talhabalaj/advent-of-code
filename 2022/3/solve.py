#!/usr/bin/env python3
import string
data = open('input.txt', 'r').read().splitlines()

priority = ' ' + string.ascii_lowercase + string.ascii_uppercase
sum = 0

for line in data:
  mid = len(line) // 2
  comp_1, comp_2 = line[:mid], line[mid:]
  we_done = False

  for i in range(mid):
    for j in range(mid):
      if comp_1[i] == comp_2[j]:
        pr = priority.index(comp_1[i])
        sum += pr
        we_done = True
        break 
    
    if we_done:
      break

print(sum)
  
