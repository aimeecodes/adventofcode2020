inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]

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

# format the data to be passed to a new function
for entry in lines:
	temp = entry.split(' ')
	limits = temp[0].split('-')

	lower = limits[0]
	upper = limits[1]
	character = temp[1].rstrip(':')
	password = temp[2]

	passwords.append([lower, upper, character, password])

def CheckPosition(pos, character, password):
	# returns 1 if character is found in pos,
	# returns 0 if character is not found in pos
	
	# split string password into temp array
	temp = list(password)

	if temp[pos] == character:
		return 1
	else:
		return 0

# initialize empty array
passwords = []

# create variable that keeps track of 
# valid passwords according to new
# interpretation of the rule

valid_passwords = 0

for pw in passwords:
	pos1 = int(pw[0]) - 1
	pos2 = int(pw[1]) - 1

	result1 = CheckPosition(pos1, pw[2], pw[3])
	result2 = CheckPosition(pos2, pw[2], pw[3])

	if (result1 + result2) == 1:
		valid_passwords += 1

print('There are ' + str(valid_passwords) + ' valid passwords.')