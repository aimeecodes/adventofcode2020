inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

# initialze numbers array
numbers = []

# first, store these in a numerical array instead of text
for l in lines:
	numbers.append(int(l))

# loop over numbers
def find2020(numbers):
	for i in range(0, len(numbers)):
		# assign number to the value at current index
		# and make sure it's an integer!!
		number1 = numbers[i]

		# check the sum of all numbers after it
		summed = 0
		for j in range(1, len(numbers)-i):
			# assign number at next value
			number2 = numbers[i+j]

			# assign their num to summed
			summed = number1 + number2

			if summed == 2020:
				return [number1, number2]
	return -1

result = find2020(numbers)

print('The result is ' + str(result[0]) + \
	"*" + str(result[1]) + '=' + str(result[0]*result[1]))