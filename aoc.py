#!/usr/bin/env python3

import os
import requests
import argparse
from datetime import datetime
import subprocess
from bs4 import BeautifulSoup
import markdownify

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
parser.add_argument('-o', '--operation', type=str,
                    default="fetch", choices=["fetch", "submit"],)
parser.add_argument('-l', '--level', type=int, default=1)

args = parser.parse_args()
year = args.year
problems = args.problems

template = """#!/usr/bin/env python3
data = open('input.txt', 'r').read().splitlines()

for line in data:
  print(line)"""


def fetch_statment(year, problem):
  url = f"https://adventofcode.com/{year}/day/{problem}"
  page = requests.get(url, headers={
      'cookie': env_map['COOKIE']
  }).text

  soup = BeautifulSoup(page, 'html.parser')
  soup.find('header').decompose()
  for each in soup.find_all('script'):
    each.decompose()
  for each in soup.find_all(id="sidebar"):
    each.decompose()
  result = markdownify.markdownify(str(soup))

  open(f"{year}/{problem}/statement.md", 'w').write(result)


def fetch(year, problems):
  for problem in problems:
    advent_url = "https://adventofcode.com/{}/day/{}/input".format(
        year, problem)
    data_input = requests.get(
        advent_url, headers={'cookie': env_map['COOKIE']}).text

    if data_input.startswith("Please don't repeatedly request this endpoint before it unlocks!"):
      print(data_input)
      return

    os.makedirs(f"{year}/{problem}", exist_ok=True)

    fetch_statment(year, problem)

    open(f"{year}/{problem}/input.txt", 'w').write(data_input)

    create_answer_file(year, problem, 1)


def create_answer_file(year, problem, level, template=template):
  file_name = f"{year}/{problem}/solve{'' if level == 1 else '_2'}.py"
  if not os.path.exists(file_name):
    open(file_name, 'w').write(template)
  os.chmod(file_name, 0o744)


def submit(year, problems, level):
  for problem in problems:
    advent_url = "https://adventofcode.com/{}/day/{}/answer".format(
        year, problem)
    file_name = os.path.join(
        os.getcwd(), f"{year}/{problem}/solve{'' if level == 1 else '_2'}.py")
    cwd = os.path.dirname(file_name)

    if not os.path.exists(file_name):
      print(f"File {file_name} does not exist for problem {problem}")
      return

    process_completed = subprocess.run(file_name, capture_output=True, cwd=cwd)
    result = process_completed.stdout
    integer = None

    try:
      integer = int(result)
    except ValueError:
      print(
          f"Result is not an integer, get {len(result)} characters of non-integer data, please only print result to stdout, using stderr for debugging")
      return

    data = {
        'level': level,
        'answer': integer,
    }

    print(f"Submitting {integer} for problem {problem} level {level}")

    data_input = requests.post(advent_url, data=data, headers={
                               'cookie': env_map['COOKIE']})
    soup = BeautifulSoup(data_input.text, 'html.parser')
    response = soup.find('article').text
    do_we_win = response.startswith("That's the right answer!")

    print(response)

    if do_we_win and level == 1:
      print("Fetching level 2 statement...")
      fetch_statment(year, problem)
      print("Fetching level 2 complete")
      create_answer_file(year, problem, 2, template=open(file_name).read())
      print("Created answer file for next level")


if args.operation == "fetch":
  fetch(year, problems)
elif args.operation == "submit":
  submit(year, problems, args.level)
else:
  print("Unknown operation")
