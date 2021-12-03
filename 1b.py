import fileinput

inc = 0
a = []
b = []
for line in fileinput.input():
  n = int(line.strip())
  if len(b) >= 3:
    b.pop(0)
  if len(a) > 0:
    b.append(n)

  print(a, b)
  if len(a) == 3 and len(b) == 3 and sum(b) > sum(a):
    inc += 1

  if len(a) >= 3:
    a.pop(0)
  a.append(n)

print(inc)