import fileinput
from collections import namedtuple

Packet = namedtuple(
    'Packet', ['version', 'type_id', 'number', 'length_type_id', 'subpackets'],
    defaults=[None, None, None])

for line in fileinput.input():
  data = line.strip()
  break

binary = ''
for char in data:
  n = int(char, 16)
  b = '{0:04b}'.format(n)
  binary += b

packets = []


def decode_packet(b, i):
  n = 0
  version = int(b[i:i + 3], 2)
  n += 3
  type_id = int(b[i + n:i + n + 3], 2)
  n += 3
  if type_id == 4:
    num = ''

    while True:
      next_blob = b[i + n:i + n + 5]
      n += 5
      num += next_blob[1:]
      if next_blob[0] == '0':
        break
    p = Packet(version=version, type_id=type_id, number=int(num, 2))
    return (n, p)

  length_type_id = int(b[i + n:i + n + 1], 2)
  n += 1
  if length_type_id == 0:
    subpacket_len = int(b[i + n:i + n + 15], 2)
    n += 15
    start = n
    subpackets = []
    while n < start + subpacket_len:
      m, subpacket = decode_packet(b[i + n:i + n + subpacket_len], 0)
      packets.append(subpacket)
      subpackets.append(subpacket)
      n += m
    p = Packet(version=version,
               type_id=type_id,
               length_type_id=length_type_id,
               subpackets=subpackets)
    return (n, p)

  if length_type_id == 1:
    num_subpackets = int(b[i + n:i + n + 11], 2)
    n += 11
    subpackets = []
    while len(subpackets) < num_subpackets:
      m, subpacket = decode_packet(b[i + n:], 0)
      packets.append(subpacket)
      subpackets.append(subpacket)
      n += m
    p = Packet(version=version,
               type_id=type_id,
               length_type_id=length_type_id,
               subpackets=subpackets)
    return (n, p)


def compute_packet(p):
  if p.type_id == 4:
    return p.number

  if p.type_id == 7:
    return 1 if compute_packet(p.subpackets[0]) == compute_packet(
        p.subpackets[1]) else 0

  if p.type_id == 6:
    return 1 if compute_packet(p.subpackets[0]) < compute_packet(
        p.subpackets[1]) else 0

  if p.type_id == 5:
    return 1 if compute_packet(p.subpackets[0]) > compute_packet(
        p.subpackets[1]) else 0

  if p.type_id == 3:
    return max(compute_packet(m) for m in p.subpackets)

  if p.type_id == 2:
    return min(compute_packet(m) for m in p.subpackets)

  if p.type_id == 0:
    return sum(compute_packet(m) for m in p.subpackets)

  if p.type_id == 1:
    product = 1
    for m in p.subpackets:
      product *= compute_packet(m)
    return product


_, main = decode_packet(binary, 0)

print(compute_packet(main))