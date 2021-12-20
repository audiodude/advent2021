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


def traverse(graph, cur, visited):
  visited.append(cur)
  if cur == 'end':
    return ','.join(visited)

  return [
      traverse(graph, e, list(visited))
      for e in graph[cur]
      if e.lower() != e or e not in visited
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