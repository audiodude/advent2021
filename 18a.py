import fileinput
import ast

numbers = []
for line in fileinput.input():
  line = line.strip()
  numbers.append(ast.literal_eval(line))


def assign(n, idx, i):
  idx = list(idx)
  m = n
  while len(idx) != 1:
    m = m[idx.pop(0)]
  m[idx[0]] = i


def at(n, idx):
  idx = list(idx)
  m = n
  while idx:
    m = m[idx.pop(0)]
  return m


def add_at(n, idx, i):
  assign(n, idx, at(n, idx) + i)


def find_right_regular_number(n, idx):
  nidx = None
  for i in range(len(idx) - 1, -1, -1):
    if idx[i] == 0:
      nidx = idx[0:i] + [1]
      break
  if nidx is not None:
    while isinstance(at(n, nidx), list):
      nidx += [0]
  return nidx


def find_left_regular_number(n, idx):
  nidx = None
  for i in range(len(idx) - 1, -1, -1):
    if idx[i] == 1:
      nidx = idx[0:i] + [0]
      break
  if nidx is not None:
    while isinstance(at(n, nidx), list):
      nidx += [1]
  return nidx


def explode(n, idx):
  left_idx = find_left_regular_number(n, idx)
  right_idx = find_right_regular_number(n, idx)

  left, right = at(n, idx)
  if left_idx is not None:
    add_at(n, left_idx, left)
  if right_idx is not None:
    add_at(n, right_idx, right)

  assign(n, idx, 0)
  return n


def requires_explode(n, idx):
  if not isinstance(n, list):
    return None
  left, right = n
  if len(idx) >= 4 and not isinstance(left, list) and not isinstance(
      right, list):
    return idx
  return requires_explode(left, idx + [0]) or requires_explode(right, idx + [1])


def split(n, idx):
  m = at(n, idx)
  pair = [m // 2, m // 2 + m % 2]
  assign(n, idx, pair)
  return n


def requires_split(n, idx):
  if not isinstance(n, list):
    if n < 10:
      return None
    else:
      return idx
  left, right = n
  requires_left = requires_split(left, idx + [0])
  if requires_left is not None:
    return requires_left
  requires_right = requires_split(right, idx + [1])
  if requires_right is not None:
    return requires_right

  return None


def red(n):
  while True:
    exp_idx = requires_explode(n, [])
    if exp_idx:
      n = explode(n, exp_idx)
      continue

    split_idx = requires_split(n, [])
    if split_idx:
      n = split(n, split_idx)
      continue

    break

  return n


def add(a, b):
  return red([a, b])


def magnitude(n):
  left, right = n
  if isinstance(left, list):
    left = magnitude(left)
  if isinstance(right, list):
    right = magnitude(right)
  return left * 3 + right * 2


for i, m in enumerate(numbers):
  if i == 0:
    n = m
    continue

  n = add(n, m)

print(magnitude(n))