inputfile = './input.txt'

with open(inputfile) as f:
	numbers = [line.rstrip('\n') for line in f]

def CanBeMade(arr, number):
	"""
	arr 		array of 25 numbers from original slice
	number 		number to see if it can be expressed as the sum
				of any combination of 2 numbers from arr
	"""

	# loop over array, find all possible sums and check against number
	for i, value1 in enumerate(arr):

		# check the sum of value and everything after it
		for j in range(1, len(arr)-i):
			# assign number at next index
			value2 = arr[i+j]

			# assign their value to summed
			summed = value1 + value2

			# check if equal to passed in number
			if summed == number:
				return True

	# if number cannot be expressed as the sum of any two numbers from arr,
	return False

# cast all members of numbers as integers
numbers = [int(x) for x in numbers]

# initialize array to hold results
results = []


# initialize upper and lower as bounds for slice
upper = 0
lower = upper + 25
idx = 25

while idx < len(numbers):
	temp = numbers[idx]

	temparr = numbers[upper:lower]

	result = CanBeMade(temparr, temp)

	results.append([numbers[idx], result, idx])

	# increase index and slices
	idx += 1
	upper += 1
	lower += 1

# initializing
idx = 0
r = True

while r == True:
	temp = results[idx]
	r = temp[1]
	idx += 1

print('The first number that does not have the desired property is ' + str(temp[0]) + '.')