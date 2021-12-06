#!/usr/bin/env python3

data = open('input.txt', 'r').read()
arr = data.split('\n')
inc_times = 0
l_arr = len(arr)

for i in range(1, l_arr):
  if arr[i] == "":
    continue
  if int(arr[i]) > int(arr[i - 1]):
    inc_times += 1

print(inc_times)
