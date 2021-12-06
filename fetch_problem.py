#!/usr/bin/env python3

import os
import requests
import argparse
from datetime import datetime

envs = open('.env').read().splitlines()
env_map = {}

for env in envs:
  key, *value = env.split('=')
  env_map[key] = "=".join(value).replace('"', '')

parser = argparse.ArgumentParser(
    description="Fetch Advent of Code Problem Data")
parser.add_argument('-y', type=int, help="The year of the problem",
                    dest="year",  default=datetime.now().year)
parser.add_argument('problems', type=int,  nargs='+',
                    metavar="problem",   help="The list of problem to fetch")

args = parser.parse_args()
year = args.year
problems = args.problems


for problem in problems:
  advent_url = "https://adventofcode.com/{}/day/{}/input".format(year, problem)
  data_input = requests.get(
      advent_url, headers={'cookie': env_map['COOKIE']}).text

  os.makedirs(f"{year}/{problem}", exist_ok=True)

  open(f"{year}/{problem}/input.txt", 'w').write(data_input)

  if not os.path.exists(f"{year}/{problem}/solve.py"):
    open(f"{year}/{problem}/solve.py", 'w').write("""
#!/usr/bin/env python3 
data = open('input.txt', 'r').read().splitlines()

for line in data:
  print(line)
    """.strip())
    os.chmod(f"{year}/{problem}/solve.py", 0o744)
