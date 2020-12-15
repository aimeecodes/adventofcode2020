inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

def GetNewPosition(right, oldposition, mapwidth):
	# returns the new position on the hill,
	# mod the map width

	# takes in
	# right 	 		movement in horizontal direction
	# oldposition 		old index position
	# mapwidth 			to mod the new position index
	return (oldposition + right) % mapwidth

def PrintStatment(slope, treecount):
	print('Using a slope of right ' + str(slope[0]) + ', down ' + \
		str(slope[1]) + ', you will encounter ' + str(treecount) + ' trees.')

# get the width of the map
mapwidth = len(lines[0])

# set an array of slopes to be checked
# note! slopes are inserted as [x, y]
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

# initialize position at the top left corner of the map
pos = 0

# initialize tree counting array
# remember that trees are considered '#'s
treecount = [0, 0, 0, 0, 0]

for index, s in enumerate(slopes):
	# set horizontal movement to s[0]
	# set vertical movement to s[1]
	hm = s[0]
	vm = s[1]

	# initialize starting position to 0
	pos = 0

	# slice lines into the lines we will encounter
	# with our vertical slope
	for l in lines[::vm]:
		temp = l[pos]

		if temp == '#':
			treecount[index] += 1

		# update position
		pos = GetNewPosition(hm, pos, mapwidth)

for index, s in enumerate(slopes):
	PrintStatment(s, treecount[index])

# initialize result to 1, to be multiplied
# by all members of treecount
result = 1

for t in treecount:
	result *= t

print(result)