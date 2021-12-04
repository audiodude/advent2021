import fileinput
from collections import defaultdict

call = None
boards = []
next_board = None
for line in fileinput.input():
  if call is None:
    call = [int(x) for x in line.strip().split(',')]
    continue

  if line.strip() == '':
    if next_board:
      boards.append(next_board)
    next_board = []
    continue
  else:
    next_board.append([int(x) for x in line.strip().split(' ') if x != ''])

called = [[] for x in range(len(boards))]
for n in call:
  for i, board in enumerate(boards):
    for y, row in enumerate(board):
      for x, spot in enumerate(row):
        if spot == n:
          called[i].append((x, y))

  winner_idx = None
  for i, call in enumerate(called):
    xs = defaultdict(int)
    ys = defaultdict(int)
    for spot in call:
      xs[spot[0]] += 1
      ys[spot[1]] += 1

    for j in range(5):
      if xs[j] == 5 or ys[j] == 5:
        winner_idx = i
        break

  if winner_idx is not None:
    winner = boards[winner_idx]
    break

all_spots = set()
for y, row in enumerate(winner):
  for x, spot in enumerate(row):
    all_spots.add((x, y))

for call in called[winner_idx]:
  all_spots.remove(call)

sum = 0
for spot in all_spots:
  sum += winner[spot[1]][spot[0]]

print(sum * n)
