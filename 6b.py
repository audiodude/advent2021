import fileinput

for line in fileinput.input():
  data = [int(x) for x in line.strip().split(',')]

fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for d in data:
  fishes[d] += 1

for i in range(256):
  new_fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i, fish in enumerate(fishes):
    if i == 0:
      new_fishes[6] += fish
      new_fishes[8] += fish
    else:
      new_fishes[i - 1] += fish
  fishes = new_fishes

print(sum(fishes))