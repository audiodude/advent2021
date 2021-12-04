import fileinput
from collections import defaultdict

readings = []
for line in fileinput.input():
  readings.append(line.strip())

o2 = None
cur_readings = readings
for i in range(12):
  if len(cur_readings) == 1:
    o2 = int(cur_readings[0], 2)
    break

  position = defaultdict(int)
  for reading in cur_readings:
    position[reading[i]] += 1

  new_readings = []
  for reading in cur_readings:
    if position['0'] > position['1']:
      if reading[i] == '0':
        new_readings.append(reading)
    elif reading[i] == '1':
      new_readings.append(reading)

  cur_readings = new_readings

co2 = None
cur_readings = readings
for i in range(12):
  if len(cur_readings) == 1:
    co2 = int(cur_readings[0], 2)
    break

  position = defaultdict(int)
  for reading in cur_readings:
    position[reading[i]] += 1

  new_readings = []
  for reading in cur_readings:
    if position['1'] < position['0']:
      if reading[i] == '1':
        new_readings.append(reading)
    elif reading[i] == '0':
      new_readings.append(reading)

  cur_readings = new_readings

print(co2 * o2)