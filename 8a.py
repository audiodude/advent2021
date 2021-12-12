import fileinput

examples = []
for line in fileinput.input():
  line = line.strip()
  pattern, output = line.split(' | ')
  examples.append((pattern.split(' '), output.split(' ')))

n = 0
for _, output in examples:
  for o in output:
    if len(o) in (2, 3, 4, 7):
      n += 1

print(n)