import fileinput
from collections import defaultdict

positions = [
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
]
for line in fileinput.input():
  for i, bit in enumerate(line.strip()):
    positions[i][bit] += 1

gamma = ''
epsilon = ''
for position in positions:
  if position['1'] > position['0']:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)