#!/usr/bin/env python3
import sys
data = open('input.txt', 'r').read().splitlines()

def print_debug(*args):
  print(*args, file=sys.stderr)

for line in data:
  print_debug(line)