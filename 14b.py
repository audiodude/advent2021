import fileinput
from collections import defaultdict

start = None
rules = []
for line in fileinput.input():
  line = line.strip()
  if start is None:
    start = line
    continue
  elif start and not line:
    continue

  rules.append(tuple(line.split(' -> ')))

active = defaultdict(int)
count = defaultdict(int)
cur = start
parts = []

for i in range(len(cur) - 1):
  parts.append('%s%s' % (cur[i], cur[i + 1]))
for p in parts:
  active[p] += 1

for char in start:
  count[char] += 1

for step in range(40):
  print('Step %s' % (step + 1))

  next_active = active.copy()
  for part, cnt in active.items():
    if cnt < 1:
      continue

    for rule in rules:
      if part == rule[0]:
        stem_1 = '%s%s' % (part[0], rule[1])
        stem_2 = '%s%s' % (rule[1], part[1])
        count[rule[1]] += cnt
        next_active[stem_1] += cnt
        next_active[stem_2] += cnt
        next_active[part] -= cnt
        break
  active = next_active

ans = sorted(list(count.items()), key=lambda x: x[1])
print(ans[-1][1] - ans[0][1])