#!/usr/bin/env python3 
data = open('input.txt', 'r').read().split('\n')

max_calc = 0
elf = {}
cur = 0

for line in data:
  if line == '':
    cur += 1
    continue

  if (cur in elf):
    elf[cur] += int(line)
  else:
    elf[cur] = int(line)

values = sorted(list(elf.values()), reverse=True)
values_sum = 0

for i in range(3):
  values_sum += values[i]


print(values_sum, values[0])