import fileinput

map = []
for line in fileinput.input():
  map.append(list(int(x) for x in line.strip()))


def neighbors(point):
  for x in (-1, 1):
    if point[0] + x >= 0 and point[0] + x < len(map[0]):
      yield (x + point[0], point[1])
  for y in (-1, 1):
    if point[1] + y >= 0 and point[1] + y < len(map):
      yield (point[0], y + point[1])


def neighbors_except(point, exclude):
  for n in neighbors(point):
    if n != exclude:
      yield n


low = 0
for y, row in enumerate(map):
  for x, point in enumerate(row):
    if all(map[adj[1]][adj[0]] > point for adj in neighbors((x, y))):
      low += point + 1

print(low)
