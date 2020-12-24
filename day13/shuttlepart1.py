import time

print('~ * ~ Day 13 Part 1 ~ * ~')

start = time.process_time()

inputfile = './input.txt'

with open(inputfile) as f:
	businfo = [line.rstrip('\n') for line in f]

earliest = int(businfo[0])

possible = businfo[1].split(',')

# clean array holding only the bus numbers, no x's
buses = [int(x) for x in possible if x != 'x']

# initialize empty array
results = []

for b in buses:
	waittime = b - (earliest % b)
	results.append(waittime)

minidx = results.index(min(results))

part1 = buses[minidx] * results[minidx]

end = time.process_time()

print('The ID of the earliest bus to the airport multiplied by ' \
	+ 'the number of minutes spent waiting is ' + str(part1))

print('Time:', round((end - start) * 1000, 3), 'ms')