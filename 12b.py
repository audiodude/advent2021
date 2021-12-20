import fileinput

data = []
for line in fileinput.input():
  data.append(line.strip().split('-'))


def build_graph():
  vertices = {}
  for pair in data:
    for v in pair:
      if v not in vertices:
        vertices[v] = []
    vertices[pair[0]].append(pair[1])
    vertices[pair[1]].append(pair[0])
  return vertices


def can_visit(e, visited):
  if e not in visited or e.lower() != e:
    return True

  if e == 'start' or e == 'end':
    return False

  smalls = [v for v in visited if v.lower() == v]
  if len(set(smalls)) == len(smalls):
    return True

  return False


def traverse(graph, cur, visited):
  visited.append(cur)
  if cur == 'end':
    return ','.join(visited)

  return [
      traverse(graph, e, list(visited))
      for e in graph[cur]
      if can_visit(e, visited)
  ]


def flatten(paths):
  ans = []
  for item in paths:
    if item:
      if isinstance(item, str):
        ans.append(item)
      else:
        ans.extend(flatten(item))
  return ans


g = build_graph()
paths = traverse(g, 'start', [])
paths = flatten(paths)
print(len(paths))