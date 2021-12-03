import fileinput

aim = 0
horiz = 0
depth = 0
for line in fileinput.input():
  line = line.strip()
  pos = line.find(' ')
  n = int(line[pos:])
  if line.startswith('forward'):
    horiz += n
    depth += aim * n
  elif line.startswith('up'):
    aim -= n
  elif line.startswith('down'):
    aim += n

print(horiz * depth)