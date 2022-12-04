#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()

overlaps = 0

for line in data:
  range_1, range_2 = line.split(',')
  range_1_start, range_1_end = range_1.split('-')
  range_2_start, range_2_end = range_2.split('-')

  range_1_start = int(range_1_start)
  range_1_end = int(range_1_end)
  range_2_start = int(range_2_start)
  range_2_end = int(range_2_end)

  if range_1_start <= range_2_start and range_1_end >= range_2_end:
    overlaps += 1
  elif range_2_start <= range_1_start and range_2_end >= range_1_end:
    overlaps += 1

print(overlaps)