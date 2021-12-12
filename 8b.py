import fileinput

examples = []
for line in fileinput.input():
  line = line.strip()
  pattern, output = line.split(' | ')
  examples.append((pattern.split(' '), output.split(' ')))

n = 0
for pattern, output in examples:
  rank = dict((i, list(pattern)) for i in range(10))

  for o in pattern:
    l = len(o)
    if l == 2:
      for r in rank:
        if r == 1:
          rank[r] = o
        elif isinstance(rank[r], list):
          rank[r].remove(o)
    elif l == 3:
      for r in rank:
        if r == 7:
          rank[r] = o
        elif isinstance(rank[r], list):
          rank[r].remove(o)
    elif l == 4:
      for r in rank:
        if r == 4:
          rank[r] = o
        elif isinstance(rank[r], list):
          rank[r].remove(o)
    elif l == 7:
      for r in rank:
        if r == 8:
          rank[r] = o
        elif isinstance(rank[r], list):
          rank[r].remove(o)
    elif l == 6:
      for r in rank:
        if r not in (0, 6, 9) and isinstance(rank[r], list):
          rank[r].remove(o)
    elif l == 5:
      for r in rank:
        if r not in (2, 3, 5) and isinstance(rank[r], list):
          rank[r].remove(o)

  for o in rank[9]:
    if all(char in o for char in rank[4]):
      rank[9] = o
      rank[0].remove(o)
      rank[6].remove(o)
      break

  for o in rank[0]:
    if all(char in o for char in rank[1]):
      rank[0] = o
      rank[6].remove(o)
      rank[6] = rank[6][0]
      break

  for o in rank[3]:
    if all(char in o for char in rank[7]):
      rank[3] = o
      rank[2].remove(o)
      rank[5].remove(o)
      break

  o = rank[5][0]
  m = 0
  for char in rank[4]:
    m += 1 if char in o else 0
  if m == 2:
    rank[2] = o
    rank[5].remove(o)
    rank[5] = rank[5][0]
  else:
    rank[5] = o
    rank[2].remove(o)
    rank[2] = rank[2][0]

  guide = dict((''.join(sorted(value)), key) for key, value in rank.items())
  decoded = ''
  for o in output:
    decoded += str(guide[''.join(sorted(o))])
  n += int(decoded)

print(n)