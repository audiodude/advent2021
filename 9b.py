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


low_points = []
sizes = []
for y, row in enumerate(map):
  for x, point in enumerate(row):
    if all(map[adj[1]][adj[0]] > point for adj in neighbors((x, y))):
      low_points.append((x, y))

for low in low_points:
  size = 1
  to_explore = list((adj, low) for adj in (neighbors(low)))
  seen = set([low])
  while to_explore:
    cur, prev = to_explore.pop()
    if map[cur[1]][cur[0]] > map[prev[1]][prev[0]]:
      seen.add(cur)
    for adj in neighbors_except(cur, prev):
      if map[adj[1]][adj[0]] == 9:
        continue
      if map[adj[1]][adj[0]] > map[cur[1]][cur[0]] and adj not in seen:
        to_explore.append(((adj[0], adj[1]), cur))
  sizes.append(len(seen))

top_3 = sorted(sizes)[-3:]
print(top_3[0] * top_3[1] * top_3[2])