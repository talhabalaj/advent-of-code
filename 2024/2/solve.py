#!/usr/bin/env python3
import sys
data = open('input.txt', 'r').read().splitlines()

def print_debug(*args):
  print(*args, file=sys.stderr)

count  = 0

for line in data:
  numbers = [int(n) for n in line.split()]
  not_safe = False
  is_increasing = True
  for idx in range(len(numbers) - 1):
    cur = numbers[idx + 1]
    pre = numbers[idx]

    if idx == 0:
      is_increasing = cur > pre
    else: 
      if cur <= pre and is_increasing:
        not_safe = True
        break
    
      if cur >= pre and not is_increasing and not( 3 > abs(cur - pre) > 0):
        not_safe = True
        break
    
      if abs(cur - pre) > 3:
        not_safe = True
        break

  print_debug(numbers, is_increasing, not_safe)
  if not not_safe:
    count += 1

print(count)