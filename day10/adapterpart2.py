from collections import deque
import numpy as np

inputfile = './input.txt'

with open(inputfile) as f:
	adapters = [int(line.rstrip('\n')) for line in f]

# create dictionary of number of nodes
# and corresponding number of paths between nodes

pathdict = {}

# initialize pathdict with length 0: entry 1
pathdict[0] = 1

def getNumberOfPaths(start, end):
	"""
	returns the number of paths possible (via addition of
	{1, 2, 3} between start and end)
	e.g. getNumberOfPaths(0,4) should return 7
	"""

	length = end - start

	# if there is no entry for this length,
	# call function to generate entry
	if pathdict.get(length) == None:
		entry = generatePaths(length)
		pathdict[length] = entry

	return pathdict[length]

def generatePaths(n):
	"""
	this function calls createAdjMatrix, and uses this generated
	adjacency matrix to calculate the number of k length paths between
	first node and last node (in this case, 0 and n)

	to do this, it must calculate A.dot(A) over and over, and pull out
	the entry at [0,n] since that's all we really care about
	"""

	# create reference copy of matrix
	A = createAdjMatrix(n)

	# create copy that can be modified
	B = createAdjMatrix(n)

	# initialize array to hold entries 
	results = []

	# append first entry to results
	results.append(A[0,n])

	for i in range(0,n):
		# generate A^i
		B = B.dot(A)

		# add the [0,n] entry to results
		results.append(B[0,n])

	return(sum(results))

def createAdjMatrix(n):
	"""
	creates an [(n+1)x(n+1)] adjacency matrix where the
	general structure is as follows:
	    0 1 1 1 0 0 ... 0
	    0 0 1 1 1 0 ... 0
	    0 0 0 1 1 1 ... 0
	A = 0 0 0 0 1 1 ... 0
	    0 0 0 0 0 1 ... 0
	    . . . . . . ... .
	    0 0 0 0 0 0 ... 1
	    0 0 0 0 0 0 ... 0

	"""
	# make a matrix of ones in the correct shape
	arr = np.ones((n+1,n+1)).astype(int)

	# section this off to only entries above the 1st diagonal
	section1 = np.triu(arr, 1)

	# make a negative version of only entries above the 4th diagonal
	section2 = -1*np.triu(arr, 4)

	# add these together to make matrix A
	A = section1 + section2
	return A

# sort the adapters numerically
adapters = sorted(adapters)

maxvolt = max(adapters)

# first find all the voltages that have a gap of 3,
# since these cannot be connected by a combination of 1s

# create stk to push each item on to for access by next item
stk = deque()

# create list of values that when encountered can only use a 
# (3) jolt to bridge
needthree = []

# start by pushing the first item onto the stk
stk.append(adapters[0])

# ignore first item, as we're dealing with it above
for item in adapters[1:]:
	previous = stk.pop()
	stk.append(item)

	# check the difference between item and previous
	diff = item - previous

	if diff == 3:
		needthree.append(previous)

# list to hold pairs of numbers to be passed into getNumberOfPaths
param = []

# generate pairs of numbers that can have adapters of 1, 2, or 3
# connecting the two joltages
i = 0
for n in needthree:
	param.append([i,n])
	i = n + 3

# add final pair to param
param.append([i, maxvolt])

# empty array to push results to
r = []

for p in param:
	r.append(getNumberOfPaths(*p))

count = np.prod(r)

print('There are ' + str(count) + ' distinct ways ' \
	+ 'to arrange your chargers to connect.')