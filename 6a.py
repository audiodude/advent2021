import fileinput

for line in fileinput.input():
  data = [int(x) for x in line.strip().split(',')]

fishes = []
new_fishes = []


class Fish:

  def __init__(self, timer=None):
    if timer is None:
      self.timer = 8
    else:
      self.timer = timer

  def iterate(self):
    global new_fishes
    self.timer -= 1
    if self.timer == -1:
      self.timer = 6
      new_fishes.append(Fish(8))


for d in data:
  fishes.append(Fish(d))

for _ in range(80):
  for fish in fishes:
    fish.iterate()
  fishes.extend(new_fishes)
  new_fishes = []

print(len(fishes))