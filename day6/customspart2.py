inputfile = './input.txt'

# need to gather all of the batch data from each
# passport and save it in a single string
with open(inputfile) as f:
	data = f.read()

# first need to separate data into each group's answers
answers = data.split('\n\n')

for idx, a in enumerate(answers):
	# first split group's answers into individuals
	answers[idx] = a.split('\n')

	# then split individuals answers into characters
	for i, item in enumerate(answers[idx]):
		answers[idx][i] = set(list(answers[idx][i]))

# initialize number of intersections
numberintersections = 0

# find set intersection of all answers
for a in answers:
	temp = set.intersection(*a)
	length = len(temp)
	print(length)
	numberintersections += length

print('The sum of each group\'s questions to which' \
	+ ' everyone answered yes is ' + str(numberintersections) + '.')