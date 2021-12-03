import fileinput

horiz = 0
depth = 0
for line in fileinput.input():
  line = line.strip()
  pos = line.find(' ')
  n = int(line[pos:])

  if line.startswith('forward'):
    horiz += n
  elif line.startswith('up'):
    depth -= n
  elif line.startswith('down'):
    depth += n

print(horiz * depth)