inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

# function that returns the number of specified
# characters in a given string
def NumberOfLetters(character, password):
	# create variable to hold number of times
	# character is found in password
	count = 0

	# create array of characters
	pass_array = list(password)

	# loop over the array, and if the indexed character
	# matches the specified one, add one to count
	for i in range(0, len(pass_array)):
		if pass_array[i] == character:
			count += 1

	# return the number of times character
	# appeared in password
	return count


# currently lines is formatted as ['a-b' character: password]
# a 			lower limit
# b 			upper limit
# character 	a-z character that specifies the rule
# password 		the associated password string

# want to remap this into 4D array where
# entry[0] = a
# entry[1] = b
# entry[2] = character
# entry[3] = password string

# initialize empty array
passwords = []

# format the data to be passed to a new function
for entry in lines:
	temp = entry.split(' ')
	limits = temp[0].split('-')

	lower = limits[0]
	upper = limits[1]
	character = temp[1].rstrip(':')
	password = temp[2]

	passwords.append([lower, upper, character, password])

# create variable that keeps track
# of the number of valid passwords
valid_passwords = 0

for pw in passwords:
	lower = int(pw[0])
	upper = int(pw[1])
	count = NumberOfLetters(pw[2], pw[3])
	if (count >= lower) & (count <= upper):
		valid_passwords += 1

print('There are ' + str(valid_passwords) + ' valid passwords.')