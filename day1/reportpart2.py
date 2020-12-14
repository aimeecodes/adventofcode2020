inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

# initialze numbers array
numbers = []

# first, store these in a numerical array instead of text
for l in lines:
	numbers.append(int(l))

# first, find all combinations that combine to under 2020
# and store these in array summedUnder2020
summedUnder2020 = []

# loop over numbers
def findUnder2020(numbers):
	global summedUnder2020
	for i in range(0, len(numbers)):
		# assign number to the value at current index
		number1 = numbers[i]

		# check the sum of all numbers after it
		summed = 0
		for j in range(1, len(numbers)-i):
			# assign number at next value
			number2 = numbers[i+j]

			# assign their num to summed
			summed = number1 + number2

			# only push to array if the sum is under
			# (2020 - smallest number in numbers) since otherwise
			# there is no way we can add anything to it without it
			# going over 2020
			limit = 2020 - min(numbers)
			if summed <= limit:
				summedUnder2020.append([number1, number2])

def find2020(inputnumber):
	for i in range(0, len(numbers)):
		# assign number to the value at current index
		# and make sure it's an integer!!
		checkingnumber = numbers[i]

		# check the sum of checking number and the 2 chosen ones
		summed = inputnumber + checkingnumber

		if summed == 2020:
			return checkingnumber
		
	return -1

# first add all numbers that sum to less than 2020 to the
# array summedUnder2020
findUnder2020(numbers)

# then, check each pair (n1, n2) against other members to see
# if they sum to 2020
for member in summedUnder2020:
	n1 = member[0]
	n2 = member[1]
	n3 = find2020(n1+n2)

	# if n3 is returned as anything except -1,
	# leave the loop
	if n3 != -1:
		break

print('The first number is ' + str(n1))

print('The second number is ' + str(n2))

print('The third number is ' + str(n3))

result = n1*n2*n3

print('Their product is ' + str(result))