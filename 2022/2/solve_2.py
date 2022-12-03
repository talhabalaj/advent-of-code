#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()
# sadly a complete rewrite of previous code.

score_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
}

science = {
    'A': {
        'win': 'B',
        'lose': 'C',
        'draw': 'A',
    },
    'B': {
        'win': 'C',
        'lose': 'A',
        'draw': 'B',
    },
    'C': {
        'win': 'A',
        'lose': 'B',
        'draw': 'C',
    },
}

strategy_score = {
  'win': 6,
  'lose': 0,
  'draw': 3,
}

what_to_do = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

p2_score = 0

for line in data:
  round_score = 0
  p1_move, strategy_code = line.split(' ')

  strategy = what_to_do[strategy_code]
  my_move = science[p1_move][strategy]
  round_score = score_dict[my_move] + strategy_score[strategy]
  p2_score += round_score


print(p2_score)
