from collections import deque
import copy
import time

print('~ * ~ Day 11 Part 2 ~ * ~')

start = time.process_time()

inputfile = './input.txt'

with open(inputfile) as f:
	oglayout = [line.rstrip('\n') for line in f]

layout = copy.deepcopy(oglayout)

# get the number of rows and number of columns
numberofrows = len(layout)
numberofcols = len(layout[0])

def isOccupied(board, i,j):
	"""
	this function takes in the position of the seat in question
	as i (row) and j (column) on the board
	returns True if == '#'
	returns False if == '.' or 'L'
	"""
	char = board[i][j]

	if char == '#':
		return True
	return False

def checkNeighbours(board, i,j):
	"""
	this function takes in the position of the seat in question
	as i (row) and j (column) on the board
	it must check all 8 directions for the first non '.' it sees
	(this behaviour could continue up to the edge of the board,
	in which case it will see no neighbour in that direction)

	'.' 		floor tile, does not change and does not count
				as occupied seat
	'L'			empty seat
	'#' 		occupied seat

	and returns a list of True / False which explain if the seats
	that it can see (in all 8 directions) are occupied
	"""

	# list of directions to modify search by
	# (starts at [1,0] and moves counterclockwise)
	directions = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]]

	# empty list to append neighbours results into
	n_list = []

	for d in directions:
		# assign variables to the direction vectors
		r = d[0]
		c = d[1]

		# init variable to hold character value
		char = '.'

		# start multiple at 1 (will grow to 2, 3, ... as needed)
		mult = 1

		while (char == '.'):
			# set values of n_row and n_col
			n_row = i + mult*r
			n_col = j + mult*c

			# run checks to see if we've reached an edge,
			# in which case break out of while loop and
			# do not append a neighbour
			if (n_row < 0) or (n_row >= numberofrows):
				break
			if (n_col < 0) or (n_col >= numberofcols):
				break

			# set char to value at board[n_row][n_col]
			char = board[n_row][n_col]

			# update mult (allows us to move into outer ring)
			mult += 1

		# check what char is: if it's
		# '#' append True
		# 'L' append False
		# '.' do nothing (means we reached the edge of a board)

		if char == '#':
			n_list.append(True)
		elif char == 'L':
			n_list.append(False)

	return n_list

def updateState(current, noccupied):
	"""
	this function returns either '#' or 'L' given 
	the current character and number of occupied neighbours
	"""
	# first if the seat is currently empty
	if current == 'L':
		if noccupied == 0:
			return '#'
		else:
			return 'L'
	if current == '#':
		if noccupied >= 5:
			return 'L'
		else:
			return '#'

def getUpdatedBoard(board):
	"""
	this returns an array which represents the new board
	it does not ever change the old one, and goes row by row,
	col by col to create a new board
	"""

	new_board = []
	for rowidx, row in enumerate(board):
		temprow = []
		thisrow = list(row)
		for colidx, col in enumerate(thisrow):
			# first check the character
			char = board[rowidx][colidx]

			# if character is '.', you can ignore it
			if char == '.':
				# append the row with the character
				temprow.append(char)
			else:
				# number of occupied neighbours
				noccupied = sum(checkNeighbours(
						board,
						rowidx,
						colidx))
				temprow.append(updateState(char,noccupied))
		new_board.append(temprow)
	return new_board

def getNumberofOccupiedSeats(board):
	"""
	takes in a board and returns the number of #s
	"""
	runningcount = 0

	for row in board:
		temp = ''.join(row)
		runningcount += temp.count('#')

	return runningcount

# create stk to hold number of occupied seats
# on previous board's state
stk = deque()

# push the number of occupied seats onto the stk
# from first state
stk.append(getNumberofOccupiedSeats(oglayout))

# initialize diff to be 1, so we can enter loop
# then diff is updated to be the difference between
# occupied seats after state is updated
diff = 1

while diff != 0:
	layout = getUpdatedBoard(layout)
	thisstate = getNumberofOccupiedSeats(layout)
	diff = thisstate - stk.pop()
	stk.append(thisstate)

print('After stabilization, there are ' + str(thisstate) + \
	' seats occupied.')


end = time.process_time()

print('Time:', round((end - start) * 1000, 3), 'ms')