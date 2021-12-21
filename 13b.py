import fileinput

fold_start = False
folds = []
points = set()
for line in fileinput.input():
  line = line.strip()
  if not fold_start:
    if not line:
      fold_start = True
      continue

    x, y = [int(n) for n in line.split(',')]
    points.add((x, y))
    continue

  folds.append((line[11], int(line.split('=')[1])))


def fold_x(points, x):
  new_points = set()
  for p in points:
    if p[0] < x:
      new_points.add(p)  # leave it alone
    else:
      new_x = x - (p[0] - x)
      new_points.add((new_x, p[1]))

  return new_points


def fold_y(points, y):
  new_points = set()
  for p in points:
    if p[1] < y:
      new_points.add(p)  # leave it alone
    else:
      new_y = y - (p[1] - y)
      new_points.add((p[0], new_y))

  return new_points


print(len(points))
for direction, coord in folds:
  method = fold_x if direction == 'x' else fold_y
  points = method(points, coord)

max_x = max(p[0] for p in points) + 1
max_y = max(p[1] for p in points) + 1

for y in range(max_y):
  for x in range(max_x):
    if (x, y) in points:
      print('#', end='')
    else:
      print('.', end='')
  print('|')