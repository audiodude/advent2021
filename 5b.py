import fileinput
from collections import defaultdict

lines = []
for line in fileinput.input():
  lines.append(line.strip())

coords = defaultdict(int)
for line in lines:
  a, b = line.split(' -> ')
  a = [int(x) for x in a.split(',')]
  b = [int(y) for y in b.split(',')]
  if a[0] == b[0]:
    order = sorted([a[1], b[1]])
    for i in range(order[0], order[1] + 1):
      coords[(a[0], i)] += 1
  elif a[1] == b[1]:
    order = sorted([a[0], b[0]])
    for i in range(order[0], order[1] + 1):
      coords[(i, a[1])] += 1
  elif abs(a[1] - b[1]) == abs(a[0] - b[0]):
    factor_0 = 1 if a[0] < b[0] else -1
    factor_1 = 1 if a[1] < b[1] else -1
    for i, j in zip(range(a[0], b[0] + factor_0, factor_0),
                    range(a[1], b[1] + factor_1, factor_1)):
      coords[(i, j)] += 1
  else:
    print('BROKEN ->', a, b)

n = 0
for coord, val in coords.items():
  if val > 1:
    n += 1

# Pretty printing
# for y in range(10):
#   for x in range(10):
#     val = coords[(x, y)]
#     if val:
#       print(val, end='')
#     else:
#       print('.', end='')
#   print()

print(n)