import time

print('~ * ~ Day 13 Part 2 ~ * ~')

start = time.process_time()

inputfile = './input.txt'

with open(inputfile) as f:
	businfo = [line.rstrip('\n') for line in f]

possible = businfo[1].split(',')

# clean array holding only the bus numbers, no x's
buses = [int(x) for x in possible if x != 'x']

end = time.process_time()

print('Time:', round((end - start) * 1000, 3), 'ms')