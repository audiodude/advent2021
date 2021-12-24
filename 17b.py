import fileinput

for line in fileinput.input():
  line = line.strip()
  parts = line[15:].split(', y=')
  target = (tuple(int(x) for x in parts[0].split('..')),
            tuple(int(y) for y in parts[1].split('..')))


def within_target(x, y):
  return x >= target[0][0] and x <= target[0][1] and y >= target[1][
      0] and y <= target[1][1]


def simulate(x_vel, y_vel):
  x = 0
  y = 0
  highest = -1000
  while True:
    if within_target(x, y):
      return highest

    if y > highest:
      highest = y

    x += x_vel
    y += y_vel
    if x_vel > 0:
      x_vel -= 1
    elif x_vel < 0:
      x_vel += 1
    y_vel -= 1

    if x > target[0][1]:
      return False

    if y < target[1][0]:
      return False


n = 0
for x in range(500):
  for y in range(-500, 500):
    result = simulate(x, y)
    if result is not False:
      n += 1
print(n)