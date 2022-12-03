#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()

hp = 0
d = 0
a = 0

for line in data:
  inst, val = line.split(' ')
  val = int(val)
  print(inst, val)
  if inst == 'forward':
    hp += val
    d += a * val
  elif inst == 'up':
    a -= val
  elif inst == 'down':
    a += val

print(hp, d, hp*d)
