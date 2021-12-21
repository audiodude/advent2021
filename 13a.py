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


print(len(fold_x(points, folds[0][1])))