import fileinput

for line in fileinput.input():
  crabs = [int(x) for x in line.strip().split(',')]

fuel = []
for i in range(max(crabs) + 1):
  cur_fuel = 0
  for crab in crabs:
    cur_fuel += abs(crab - i)
  fuel.append(cur_fuel)

min_fuel = min(fuel)
print(min_fuel)