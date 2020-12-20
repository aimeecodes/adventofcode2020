from collections import deque

inputfile = './input.txt'

with open(inputfile) as f:
	adapters = [int(line.rstrip('\n')) for line in f]

# sort the adapters numerically
adapters = sorted(adapters)

# create variables to hold 1diffcount and 3diffcount
# both automatically start at one because
# one is between the socket (1), and the other is between your phone (3)
onediffcount = 1
threediffcount = 1

# create stk to push each item on to for access by next item
stk = deque()

# start by pushing the first item onto the stk
stk.append(adapters[0])

# ignore first time, as we're dealing with it above
for item in adapters[1:]:
	previous = stk.pop()
	stk.append(item)

	# check the difference between item and previous
	diff = item - previous

	if diff == 1:
		onediffcount += 1
	elif diff == 3:
		threediffcount += 1

print('There are ' + str(onediffcount) + ' differences of 1 jolt' + \
		' and ' + str(threediffcount) + ' differences of 3 jolts.')

print(str(onediffcount*threediffcount))