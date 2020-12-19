import copy
from collections import deque

inputfile = './input.txt'

with open(inputfile) as f:
	steps = [line.rstrip('\n') for line in f]

def ChangePosition(current, adjust):
	"""
	takes in the current position and returns
	the adjusted position
	"""
	return current + adjust

# create a table where
# item[0] 'nop', 'acc', 'jmp'	
# item[1] '+', '-'
# item[2] integer
# item[3] visited flag, initialized as false

table = []
for s in steps:
	string = s[:3]
	sign = s[4]
	adjust = s[5:]
	table.append([string, sign, adjust, False])

def StartTrawling(idx, table, change):
	"""
	idx 		starting position

	table 		table containing the steps which can be changed
				as idx moves through the table

	change 		idx that will be changed from either 'nop' > 'jmp'
				or 'jmp' to 'nop'
	
	returns array of size 2
	[0] 	idx of final call made before either running into
			already encountered step, or idx of 613
	[1] 	accumulated
	"""

	# initialize acc as 0
	acc = 0

	# make a copy of values (not references) of table
	# so changes made in this function will not reflect on
	# original table
	t = copy.deepcopy(table)

	# first make the change at the specified idx
	temp = t[change]

	if temp[0] == 'jmp':
		t[change][0] = 'nop'
	elif temp[0] == 'nop':
		t[change][0] = 'jmp'

	while t[idx][3] == False:
		# first change visited status
		t[idx][3] = True
		# visited.append(idx)

		# there are 3 possibilities for item[0],
		# check which it is and decide what to do
		# based on this value
		if t[idx][0] == 'nop':
			# increase idx by one, and
			# return to start of loop
			idx += 1

		elif t[idx][0] == 'acc':
			# save accumulator adjustment variable
			# to accadjust
			accadjust = int(table[idx][2])

			# modify it based on + / -
			if t[idx][1] == '-':
				accadjust *= -1
			# increase the acc variable by value
			# at table[idx][2]
			acc += accadjust

			# increase idx by 1
			idx += 1

		elif t[idx][0] == 'jmp':
			# get the adjustment variable
			adjust = int(t[idx][2])

			# modify it based on + / -
			if t[idx][1] == '-':
				adjust *= -1

			# update the index using ChangePosition
			idx = ChangePosition(idx, adjust)

		# check new idx: if new idx is out of bounds == len(steps),
		# break out and return this idx as it will mean the program terminates
		# properly with this changed input
		if idx == len(table):
			break
	r = [idx, acc]
	return r

# make a stack holding the idx of each call that is either 'jmp' or 'nop'
stk = deque()

# initialize index
idx = 0

# initialize firstacc
firstacc = 0

# create table that can be adjusted for first run index tracking
firstrun = copy.deepcopy(table)

while firstrun[idx][3] == False:
	# first change visited status
	firstrun[idx][3] = True

	# there are 3 possibilities for item[0],
	# check which it is and decide what to do
	# based on this value
	if firstrun[idx][0] == 'nop':
		# increase idx by one, and
		# return to start of loop
		idx += 1

		# push to stk to revisit
		stk.append(idx)

	elif firstrun[idx][0] == 'acc':
		# save accumulator adjustment variable
		# to accadjust
		accadjust = int(firstrun[idx][2])

		# modify it based on + / -
		if firstrun[idx][1] == '-':
			accadjust *= -1

		# increase the acc variable by value
		# at firstrun[idx][2]
		firstacc += accadjust

		# increase idx by 1
		idx += 1

	elif firstrun[idx][0] == 'jmp':
		# get the adjustment variable
		adjust = int(firstrun[idx][2])

		# modify it based on + / -
		if firstrun[idx][1] == '-':
			adjust *= -1

		# push to stk to revisit
		stk.append(idx)

		# update the index using ChangePosition
		idx = ChangePosition(idx, adjust)

returned = 0

while returned != 613:
	temp = stk.pop()
	arr = StartTrawling(0, table, temp)
	returned = arr[0]

print('Step ' + str(temp) + ' must be changed in order for the program to terminate.')
print('Value of acc after changing step ' + str(temp) + ': ' + str(arr[1]))