#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()

p1_move_dict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

p2_move_dict = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

score_dict = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

p2_score = 0

for line in data:
  p1_move, p2_move = line.split(' ')
  p1_move_normalised, p2_move_normalized = [
      p1_move_dict[p1_move], p2_move_dict[p2_move]]

  print(f'p1_move: {p1_move_normalised}, p2_move: {p2_move_normalized}')

  round_score = score_dict[p2_move_normalized]

  if p1_move_normalised == p2_move_normalized:
    round_score += 3  # draw

  if p1_move_normalised == 'scissors' and p2_move_normalized == 'rock':
    round_score += 6  # win

  if p1_move_normalised == 'rock' and p2_move_normalized == 'paper':
    round_score += 6  # win

  if p1_move_normalised == 'paper' and p2_move_normalized == 'scissors':
    round_score += 6  # win

  print(f'round_score: {round_score}')

  p2_score += round_score


print(p2_score)
