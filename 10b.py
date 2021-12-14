import fileinput

codes = []
for line in fileinput.input():
  codes.append(line.strip())

char_to_score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
matching = (('(', ')'), ('[', ']'), ('{', '}'), ('<', '>'))
scores = []
for code in codes:
  stack = []
  found_error = False
  for x in code:
    if x in ('(', '[', '{', '<'):
      stack.append(x)
    else:
      found_error = False
      for data in matching:
        if x == data[1]:
          if stack[-1] != data[0]:
            found_error = True
          else:
            stack.pop()
      if found_error:
        break

  if found_error:
    continue

  score = 0
  for s in reversed(stack):
    score *= 5
    score += char_to_score[s]
  scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
