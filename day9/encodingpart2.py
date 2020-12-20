inputfile = './input.txt'

with open(inputfile) as f:
	numbers = [line.rstrip('\n') for line in f]

# cast all members of numbers as integers
numbers = [int(x) for x in numbers]

# initialize special number variable which holds the
# number which is the sum of a contiguous set of at least
# 2 numbers from input

# note - need to add way to port this over from part 1
special = 133015568

# index of special number
spidx = 572

# know we don't need to go past spidx, since everything
# it will yield an even larger sum than special
# (since special would be included by default)

def findUpperandLower(numbers):
	# just go over the entire array
	for i in range(0, spidx):
		for j in range(i+1, spidx):
			testsum = sum(numbers[i:j])

			if testsum == special:
				return [i, j]
	return [-1, -1]

# want to come back and write a function
# that doesn't go straight to brute force

results = findUpperandLower(numbers)

upper = results[0]
lower = results[1]

# find the min / max in slice between upper and lower
minimum = min(numbers[upper:lower])
maximum = max(numbers[upper:lower])

print('Encryption weakness: ' + str(minimum + maximum))