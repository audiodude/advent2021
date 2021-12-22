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


def assemble(parts):
  ans = ''
  for i, part in enumerate(parts):
    if i == 0:
      ans += part
    else:
      ans += part[1:]
  return ans


cur = start
for _ in range(10):
  parts = []
  for i in range(len(cur) - 1):
    parts.append('%s%s' % (cur[i], cur[i + 1]))

  for rule in rules:
    new_parts = []
    for part in parts:
      if part == rule[0]:
        new_parts.append(''.join([part[0], rule[1], part[1]]))
      else:
        new_parts.append(part)  # leave it alone
    parts = new_parts

  cur = assemble(parts)
  print(cur)

count = defaultdict(int)
for c in cur:
  count[c] += 1

ans = sorted(list(count.items()), key=lambda x: x[1])
print(ans[-1][1] - ans[0][1])