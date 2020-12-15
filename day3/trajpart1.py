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

# get the width of the map
mapwidth = len(lines[0])

# set the horizontal movement to 3
hm = 3

# initialize position at the top left corner of the map
pos = 0

# initialize tree counting variable
# remember that trees are considered '#'s
treecount = 0

# run through lines, and check the character
# at each new position
for l in lines:
	temp = l[pos]

	if temp == '#':
		treecount += 1

	pos = GetNewPosition(hm, pos, mapwidth)

print('Using a slope of right 3 and down 1, you will encounter ' + \
		str(treecount) + ' trees.')