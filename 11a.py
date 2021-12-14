import fileinput

map = []
for line in fileinput.input():
  map.append(list(int(x) for x in line.strip()))


def neighbors(point_x, point_y):
  point = (point_x, point_y)
  for x in (-1, 0, 1):
    for y in (-1, 0, 1):
      if (not (x == 0 and y == 0) and point[1] + y >= 0 and
          point[1] + y < len(map) and point[0] + x >= 0 and
          point[0] + x < len(map[0])):
        yield (x + point[0], y + point[1])


def neighbors_except(point_x, point_y, ex):
  for n in neighbors(point_x, point_y):
    if n[0] != ex[0] and n[1] != ex[1]:
      yield n


def pretty_print():
  for row in map:
    for point in row:
      print(point, end='')
    print()


ans = 0
for i in range(100):
  for y in range(len(map)):
    for x in range(len(map[0])):
      map[y][x] += 1

  flashed = True
  while flashed:
    flashed = False
    for y in range(len(map)):
      for x in range(len(map[0])):
        if map[y][x] > 9:
          flashed = True
          ans += 1
          map[y][x] = 0
          for n in neighbors(x, y):
            if map[n[1]][n[0]] != 0:
              map[n[1]][n[0]] += 1

print(ans)