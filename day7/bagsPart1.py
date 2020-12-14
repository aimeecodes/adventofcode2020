from collections import deque

inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

rules = []
# max_length = 0

# strip out the '.' at the end of the lines, and split each line
# into an array of strings
for l in lines:
	l = l.rstrip('.')
	rules += [str.split(l)]

# create a stack to keep track of all the bags which
# contain a shiny gold bag
bigstk = deque()

# this function will return a stack with all the names of the
# bags which contain bagname
def CheckBags(bagname):

	# create new stack for this specific string / bagname
	stk = deque()

	for r in rules:
		# put string back together, so we can see if whatever
		# bag description + bag color appear next to each other
		# anywhere in the string
		str = ' '
		str = str.join(r[4:])

		# if this string contains bagname, add the containing
		# bag to the stack
		if bagname in str:
			stk.append(r[0] + ' ' + r[1])
	return stk

bigstk = CheckBags('shiny gold')
bagset = set()

while len(bigstk) > 0:
	# add whatever bag that is in the popping position to our bagset
	# (since it is a set, if it has already been added, we won't
	# double count)
	bagset.add(bigstk[-1])

	# make a temporary stk to hold the returned strings
	tmpstk = CheckBags(bigstk.pop())

	# push all items off tmpstk onto the bigstk (to be iterated over)
	while len(tmpstk) > 0:
		bigstk.append(tmpstk.pop())

print('There are ' + str(len(bagset)) + ' bags that can hold a shiny gold bag.')