import fileinput

codes = []
for line in fileinput.input():
  codes.append(line.strip())

matching = (('(', ')', 3), ('[', ']', 57), ('{', '}', 1197), ('<', '>', 25137))
ans = 0
for code in codes:
  stack = []
  for x in code:
    if x in ('(', '[', '{', '<'):
      stack.append(x)
    else:
      found_error = False
      for data in matching:
        if x == data[1]:
          if stack[-1] != data[0]:
            ans += data[2]
            found_error = True
          else:
            stack.pop()
      if found_error:
        break

print(ans)