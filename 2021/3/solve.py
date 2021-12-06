#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()

bitlength = len(data[0])
gamma = ""
ep = ""

for bit_idx in range(0, bitlength):
  ones = 0
  zeros = 0
  for line in data:
    bit = line[bit_idx]
    if bit == '0':
      zeros += 1
    else:
      ones += 1
  if ones > zeros:
    gamma += '1'
    ep += '0'
  else:
    ep += '1'
    gamma += '0'

print(int(gamma, 2) * int(ep, 2))
