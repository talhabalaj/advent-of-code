#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()

bitlength = len(data[0])
start = True

ones = []
zeros = []

for bit_idx in range(0, bitlength):
  if start:
    for line in data:
      bit = line[bit_idx]
      if bit == '0':
        zeros.append(line)
      else:
        ones.append(line)
    start = False
  else:
    for line in e:
      bit = line[bit_idx]
      if bit == '0':
        ones.append(line)
      else:
        zeros.append(line)

print(int(gamma, 2) * int(ep, 2))
