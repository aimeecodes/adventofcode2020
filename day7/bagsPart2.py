from collections import deque

inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

rules_array = []

# strip out the '.' at the end of the lines, and split each line
# into an array of strings
for l in lines:
	l = l.rstrip('.')
	rules_array += [str.split(l)]


# create dictionary so each bag's rules can be looked up quickly
rules = dict()

# create global runningsum array
runningsum = []

for r in rules_array:
	name = r[0] + ' ' + r[1]
	rules[name] = r[4:]

# pass this the name of the bag you need the number
# of types of bags it contains (1-4)
def GetNumberOfTypesOfBags(bagname):
	arr = rules[bagname]
	bagnumber = int(len(arr) / 4)
	return bagnumber

def AnyMoreBagsInside(bagname):
	# takes in the name of a bag, returns boolean
	# returns True if there are no more bags inside
	# returns False if there are more bags inside

	if rules[bagname][0] == 'no':
		return False
	return True

def BagsDirectlyInside(bagname):
	# takes in bagname (e.g. 'shiny gold' 'dotted red' etc),
	# returns a single stack with directly held bags 
	# 	(e.g. shiny gold should return a stack that looks like this: 
	# 	['pale brown', 'pale brown', 'dotted chartreuse',
	# 	'dotted chartreuse', 'vibrant gold', 'dull mag', 'dull mag',
	# 	'dull mag', 'dull mag'])

	# numstk 	has the numbers associated to the contained bags
	# namestk 	has the names associated to the contained bags
	# stk 		has the final stack that holds all bags that are
	# 			directly inside bagname

	numstk = deque()
	namestk = deque()
	stk = deque()

	# get the dictionary entry of the bagname
	entry = rules[bagname]

	# get the number of types of bags of this bagname
	bagnumber = GetNumberOfTypesOfBags(bagname)

	# loop over contained number of types of bags to get [amount] and [bagname]
	# then push these onto their respective stacks
	for i in range(0, bagnumber):
		numstk.append(entry[i*4])
		namestk.append(str(entry[i*4 + 1] + ' ' + str(entry[i*4 + 2])))

	# fill stk with the correct number of bagnames
	while len(numstk) > 0:
		num = int(numstk.pop())
		name = namestk.pop()
		for i in range(0,num):
			stk.append(name)

	return stk

def GetNumber(bagname):
	# initialize variable that tells you how many bags are inside bagname
	bags_inside = 0

	# create a stack of all directly contained bags
	stk = BagsDirectlyInside(bagname)

	# while loop that depends on stk emptying
	while len(stk) > 0:
		temp = stk.pop()

		# automatically add one bag
		bags_inside += 1

		# check if temp has any bags inside
		# if no more bags are inside,
		# return to start of loop
		# if more bags are inside, call this function on the temp bag

		if AnyMoreBagsInside(temp):
			bags_inside += GetNumber(temp)

	# outside while loop, get here when stk is empty
	# and there are no more bags to check

	return bags_inside

desired_bag = 'shiny gold'

result = GetNumber(desired_bag)

print('There are ' + str(result) + \
	' bags inside 1 ' + str(desired_bag) + ' bag.')