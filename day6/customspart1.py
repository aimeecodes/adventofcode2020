inputfile = './input.txt'

# need to gather all of the batch data from each
# passport and save it in a single string
with open(inputfile) as f:
	data = f.read()

# first need to separate data into each group's answers
answers = data.split('\n\n')

for idx, a in enumerate(answers):
	answers[idx] = a.replace('\n', '')

# initialize list of sets
setlist = []

# loop over answers, add each group's set of responses
# to setlist

for a in answers:
	# initialize set to hold group's positive responses
	group = set()

	temp = list(a)

	for char in temp:
		group.add(char)
	setlist.append(group)

# initialize variable to hold count of positive questions
pQcount = 0

for item in setlist:
	temp = len(item)
	pQcount += temp

print('The sum of the counts of questions '\
	+ 'to which anyone answered "yes" for all groups is '\
	 + str(pQcount) + '.')