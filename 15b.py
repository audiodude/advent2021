import fileinput
from collections import defaultdict

grid = []
for line in fileinput.input():
  grid.append(list(int(x) for x in line.strip()))


def neighbors(point):
  for x in (-1, 1):
    if point[0] + x >= 0 and point[0] + x < len(grid[0]) * 5:
      yield (x + point[0], point[1])
  for y in (-1, 1):
    if point[1] + y >= 0 and point[1] + y < len(grid) * 5:
      yield (point[0], y + point[1])


def lookup(point):
  delta_x = point[0] // len(grid[0])
  delta_y = point[1] // len(grid)
  raw = grid[point[1] % len(grid[0])][point[0] % len(grid)] + delta_x + delta_y
  if raw < 10:
    return raw
  else:
    return (raw + 1) % 10


graph = {}
for y in range(len(grid) * 5):
  for x in range(len(grid[0]) * 5):
    graph[(x, y)] = list(neighbors((x, y)))

q = set(graph.keys())
dist = {}
prev = {}

while q:
  shortest = sorted(list(
      (point, dist) for (point, dist) in dist.items() if point in q),
                    key=lambda pair: pair[1])
  if len(shortest) < 1:
    u = (0, 0)
  else:
    u = shortest[0][0]

  q.remove(u)
  if len(q) % 1000 == 0:
    print(len(q))

  if u == (len(grid[0]) * 5 - 1, len(grid) * 5 - 1):
    break

  for v in graph[u]:
    if v not in q:
      continue

    alt = dist.get(u, 0) + lookup((v[1], v[0]))
    if alt < dist.get(v, alt + 1):
      dist[v] = alt
      prev[v] = u

n = 0
point = ((len(grid[0]) * 5 - 1, len(grid) * 5 - 1))
while True:
  n += lookup((point[1], point[0]))
  point = prev[point]
  if point == (0, 0):
    break

print(n)