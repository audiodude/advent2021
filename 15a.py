import fileinput
from collections import defaultdict

grid = []
for line in fileinput.input():
  grid.append(list(int(x) for x in line.strip()))


def neighbors(point):
  for x in (-1, 1):
    if point[0] + x >= 0 and point[0] + x < len(grid[0]):
      yield (x + point[0], point[1])
  for y in (-1, 1):
    if point[1] + y >= 0 and point[1] + y < len(grid):
      yield (point[0], y + point[1])


graph = {}
for y, row in enumerate(grid):
  for x, weight in enumerate(row):
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

  if u == (len(grid[0]) - 1, len(grid) - 1):
    break

  for v in graph[u]:
    if v not in q:
      continue

    alt = dist.get(u, 0) + grid[v[1]][v[0]]
    if alt < dist.get(v, alt + 1):
      dist[v] = alt
      prev[v] = u

n = 0
point = ((len(grid[0]) - 1, len(grid) - 1))
while True:
  n += grid[point[1]][point[0]]
  point = prev[point]
  if point == (0, 0):
    break

print(n)