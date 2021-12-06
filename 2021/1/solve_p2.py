#!/usr/bin/env python3

arr = list(map(int, open('input.txt', 'r').read().splitlines()))
inc_times = 0
l_arr = len(arr)


for i in range(1, l_arr):
  s = sum(arr[i:i+3])
  prev = sum(arr[i-1:i+2])
  print(" + ".join(map(str, arr[i:i+3])), '=', s)
  if s > prev:
    inc_times += 1

print(inc_times)
