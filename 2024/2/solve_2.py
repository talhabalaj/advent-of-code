#!/usr/bin/env python3
import sys
data = open('input.txt', 'r').read().splitlines()

def print_debug(*args):
  print(*args, file=sys.stderr)

def is_safe(levels):
    # Convert string numbers to integers
    nums = [int(x) for x in levels.split()]
    
    # Check if differences between adjacent numbers are between 1 and 3
    differences = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    if not all(1 <= abs(d) <= 3 for d in differences):
        return False
    
    # Check if sequence is consistently increasing or decreasing
    return all(d > 0 for d in differences) or all(d < 0 for d in differences)

def solve(input_data):
    # Split input into lines and remove empty lines
    reports = [line.strip() for line in input_data if line.strip()]
    
    # Count safe reports
    safe_count = sum(1 for report in reports if is_safe(report))
    
    return safe_count

print(solve(data))