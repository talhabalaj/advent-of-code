#!/usr/bin/env python3
import sys
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

arr1.sort()
arr2.sort()

total = 0

for a, b in zip(arr1, arr2):
  distance = abs(a - b)
  total += distance
  print_debug(a, b, distance)

print(total)