inputfile = './input.txt'

with open(inputfile) as f:
	steps = [line.rstrip('\n') for line in f]

# initialize accumulation variable
acc = 0

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

# initialize index
idx = 0

while table[idx][3] == False:
	# first change visited status
	table[idx][3] = True

	# there are 3 possibilities for item[0],
	# check which it is and decide what to do
	# based on this value
	if table[idx][0] == 'nop':
		# increase idx by one, and
		# return to start of loop
		idx += 1

	elif table[idx][0] == 'acc':
		# save accumulator adjustment variable
		# to accadjust
		accadjust = int(table[idx][2])

		# modify it based on + / -
		if table[idx][1] == '-':
			accadjust *= -1
		# increase the acc variable by value
		# at table[idx][2]
		acc += accadjust

		# increase idx by 1
		idx += 1

	elif table[idx][0] == 'jmp':
		# get the adjustment variable
		adjust = int(table[idx][2])

		# modify it based on + / -
		if table[idx][1] == '-':
			adjust *= -1

		# update the index using ChangePosition
		idx = ChangePosition(idx, adjust)

print('Current acc value is ' + str(acc) + '.')