inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

# initialze numbers array
numbers = [int(x) for x in lines]

# loop over numbers
def find2020(numbers):
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

			if summed == 2020:
				return [number1, number2]
	return -1

result = find2020(numbers)

n1 = result[0]
n2 = result[1]
product = n1*n2

print('The result is ' + str(n1) + \
	"*" + str(n2) + '=' + str(product))