import fileinput

inc = 0
n = None
for line in fileinput.input():
  m = int(line.strip())
  if n is not None and m > n:
    inc += 1
  n = m

print(inc)