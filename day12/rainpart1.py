import time

print('~ * ~ Day 12 Part 1 ~ * ~')
start = time.process_time()

inputfile = './input.txt'

with open(inputfile) as f:
	instructions = [line.rstrip('\n') for line in f]

# initialize X and Y coordinates
# (X = East / West, Y = North / South)
Xcoord = 0
Ycoord = 0
currentheading = 'E'

# note directions are labeled as theta on unit circle
# moving counterclockwise
dirdict = {'E': 0, 'N': 90, 'W': 180, 'S': 270}

# create inverse dictionary to move back from angle coord to char
ivdirdict = dict((v, k) for k, v in dirdict.items())

def parseLine(string):
	letter = string[0]
	value = string[1:]
	return [letter, value]

def makeAdjustments(character, value):
	global Xcoord, Ycoord, currentheading
	"""
	takes in a character [ N, S, E, W, L, R, F ]
	and a value (numerical)
	does not return anything, but adjusts Xcoord, Ycoord, and currentheading
	"""

	# handle turns
	if (character == 'L') or (character == 'R'):
		currentheading = turn(currentheading, character, value)

	# handle forward instructions
	if character == 'F':
		# pass currentheading and value into move
		move(currentheading, value)

	# handle X movements
	if (character == 'E') or (character == 'W'):
		moveX(character, value)

	if (character == 'N') or (character == 'S'):
		moveY(character, value)

def move(character, value):
	if character == 'S' or character == 'N':
		moveY(character, value)
	else:
		moveX(character, value)

def moveY(character, value):
	"""
	takes in either 'S' or 'N' and adjusts position
	"""

	global Ycoord
	if character == 'S':
		value *= -1
	Ycoord += value

def moveX(character, value):
	"""
	takes in either 'E' or 'W' and adjusts position
	"""

	global Xcoord
	if character == 'W':
		value *= -1
	Xcoord += value	

def turn(currentheading, turndirection, degrees):
	"""
	takes currentheading [ 'E', 'W', 'N', 'S' ] 
	the turning direction              [ R, L ] 
	the degrees of the turn    [ 90, 180, 270 ]
	returns a newheading    [ 0, 90, 180, 270 ]
	"""
	currentheading = dirdict[currentheading]

	if turndirection == 'R':
		degrees *= -1

	newheading = (currentheading + degrees) % 360

	return ivdirdict[newheading]

for i in instructions:
	# parse line
	r = parseLine(i)
	makeAdjustments(r[0], int(r[1]))

M = abs(Xcoord) + abs(Ycoord)

end = time.process_time()

print('The Manhattan distance between that location and' \
	+ ' the ship\'s starting position is ' + str(M) + '.')

print('Time:', round((end - start) * 1000, 3), 'ms')
