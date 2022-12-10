#!/usr/bin/env python3
import sys
import os
[puzzle, ops] = open('input.txt', 'r').read().split('\n\n')


def print_debug(*args, **kwargs):
  print(*args, **kwargs, file=sys.stderr)


def parse_puzzle(puzzle):
  puzzle = puzzle.split('\n')

  r = []

  for line in puzzle:
    cur = []
    for i in range(0, len(line), 4):
      cur.append(line[i:i+3])
    r.append(cur)

  tr = []

  for i in range(len(r)):
    tr.append([])
    for j in range(len(r[i])):
      tr[i].append(r[j][i])

  for i in range(len(tr)):
    tr[i] = list(filter(lambda x: x != '   ', tr[i][::-1]))
  
  return tr

puzzle_matrix = parse_puzzle(puzzle)




for line in ops.split('\n'):
  if (line == ''): continue
  ___, amount, __, fr, _, to = line.split(' ')
  amount = int(amount) 
  fr = int(fr) - 1   
  to = int(to) - 1 


  if (amount == 0): continue

  for line in puzzle_matrix:
    print_debug(line)
  
  print_debug({
    'amount': amount,
    'fr': fr,
    'to': to
  })

  for i in range(amount):
    puzzle_matrix[to].append(puzzle_matrix[fr].pop())

r = ''

for line in puzzle_matrix:
  r+= line[-1][1]

print(r)