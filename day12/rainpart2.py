import time
import numpy as np

print('~ * ~ Day 12 Part 2 ~ * ~')
start = time.process_time()

inputfile = './input.txt'

with open(inputfile) as f:
	instructions = [line.rstrip('\n') for line in f]

# initialize vectors that represent ship's current position
# and the waypoint position
ship_pos = np.array([0,0]).astype(int)
wp_slope = np.array([10,1]).astype(int)

# note directions are labeled as theta on unit circle
# moving counterclockwise
dirvectordict = {'E': np.array([1,0]).astype(int),
				'N': np.array([0,1]).astype(int),
				'W': np.array([-1,0]).astype(int),
				'S': np.array([0,-1]).astype(int)
				}

dirrotatedict = {90: np.array([[0, -1],[1, 0]]),
				180: np.array([[-1, 0],[0, -1]]),
				270: np.array([[0, 1],[-1, 0]])
				}

dirdict = {'E': 0, 'N': 90, 'W': 180, 'S': 270}

# create inverse dictionary to move back from angle coord to char
ivdirdict = dict((v, k) for k, v in dirdict.items())

def updateShipPos(wp_slope, value):
	'''
	this is called when a 'F' is encountered and we need to
	move the ship towards the waypoint by a specific number of values
	'''
	global ship_pos
	ship_pos += value * wp_slope

def udpateWPSlope(direction, value):
	'''
	this is called when one of the following is encountered:
	[ 'E', 'N', 'W', 'S' ] >> translated into 
	'E' 		 [1,0]
	'N'			 [0,1]
	'W'			[-1,0]
	'S'			[0,-1]
	and added as value multiple to wp_slope
	'''
	global wp_slope
	wp_slope += value * dirvectordict[direction]

def rotateWPSlope(direction, value):
	'''
	this is called when 'L' or 'R' is encountered
	and we need to rotate wp_slope
	'''
	global wp_slope

	# use opposite operation if going in clockwise direction
	if direction == 'L':
		value = (value*-1) % 360

	wp_slope = wp_slope.dot(dirrotatedict[value])

def parseLine(string):
	'''
	this gets called on every line of instruction, it returns
	the instructions as [character, value]
	'''
	character = string[0]
	value = string[1:]
	return [character, value]

def makeDecision(string):
	global wp_slope, ship_pos
	r = parseLine(string)
	character = r[0]
	value = int(r[1])

	# handle if character is 'L' or 'R'
	if (character == 'L') or (character == 'R'):
		rotateWPSlope(character, value)
	# handle if character if 'F'
	elif character == 'F':
		updateShipPos(wp_slope, value)
	# last case, if character is [ 'N' 'S' 'E' 'W' ]
	else:
		udpateWPSlope(character, value)

for i in instructions:
	makeDecision(i)

end = time.process_time()

M = abs(ship_pos[0]) + abs(ship_pos[1])

print('The Manhattan distance between that location and' \
	+ ' the ship\'s starting position is ' + str(M) + '.')

print('Time:', round((end - start) * 1000, 3), 'ms')
