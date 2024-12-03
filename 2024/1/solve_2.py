#!/usr/bin/env python3
import sys
from collections import Counter
data = open('input.txt', 'r').read().splitlines()

def print_debug(*args):
  print(*args, file=sys.stderr)


arr1 = []
arr2 = []

for line in data:
  a, b, *_ = line.split()
  a, b = int(a), int(b)
  
  arr1.append(a)
  arr2.append(b)

arr2_counter = Counter(arr2)

total = 0

for a in arr1:
  total += arr2_counter[a] * a
  print_debug(a, arr2_counter[a])

print(total)