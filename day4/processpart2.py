inputfile = './input.txt'

# need to gather all of the batch data from each
# passport and save it in a single string
with open(inputfile) as f:
	data = f.read()

# first need to separate data into individual passports
passports = data.split('\n\n')

def CleanUpEntry(str):
	"""
	this function should take in an individual's passport
	string, strip it of any '\n' characters, and return
	an array of data with a -1 where data is missing:
	byr 	[Birth Year]
	iyr 	[Issue Year]
	eyr 	[Expiration Year]
	hgt 	[Height]
	hcl 	[Hair Color]
	ecl 	[Eye COlor]
	pid 	[Passport ID]
	cid 	[Country ID]
	"""
	str = str.replace('\n', ' ')

	# split the cleaned string into an array 
	arr = str.split()

	# rearrange the items in alphabetical order
	arr = sorted(arr)

	return arr

def LengthTest(arr):
	"""
	this function will decide if a passport has the correct
	amount of fields present in order to be valid
	Valid Length 	length of 8, all fields present
	Valid Length 	length of 7, only missing 'cid' field
	Invalid Length 	
	Valid Length returns True,
	Invalid Length returns False

	first it checks the length of the array:
		length == 8 	> valid
		length == 7 	> passed to another function to see which field
						is missing
		length <= 6 	> not valid
	"""
	if len(arr) == 8:
		return True;
	elif len(arr) == 7:
		return IsMissingField('cid', arr)
	else:
		return False

def IsMissingField(field, arr):
	"""
	this function returns a True or False value, depending
	on if the array is missing a field that starts with the
	value passed in through field
	"""
	for a in arr:
		temp = a[0:3]
		if temp == field:
			return False
	return True

def NumberTest(num, lower, upper):
	"""
	takes in number, checks if it is between
	lower and upper
	"""

	# run the check
	if (num >= lower) & (num <= upper):
		return True
	return False

def HeightTest(string):
	"""
	Checks the last 2 characters to see if they are
	cm or in or not specified, and is passed to
	NumberTest with the appropriate parameters
	"""
	# pull out the last 2 characters of the string
	unit = string[-2:]

	# if there are no units (unit is not 'in' or 'cm')
	# return False
	if (unit != 'in') & (unit != 'cm'):
		return False

	# pull out the measurement, cast as integer
	measurement = int(string[:-2])

	if unit == 'cm':
		return NumberTest(measurement, 150, 193)
	if unit == 'in':
		return NumberTest(measurement, 59, 76)
	return False

def HairColorTest(str):
	"""
	Checks 3 things:
	[1] len(str) 	should be 7 (including #)
	[2] str[0] 		should be '#'
	[3] str[1:] 	should be in specific array of characters
	"""

	allowedchar = ['0', '1', '2', '3', '4', '5', '6', '7',
					'8', '9', 'a', 'b','c', 'd', 'e', 'f']

	length = len(str)
	if length != 7:
		return False

	if str[0] != '#':
		return False

	lastsix = list(str[1:])

	for char in lastsix:
		if not(char in allowedchar):
			return False
	return True

def EyeColorTest(str):
	"""
	checks if input is equal to one of 
	the valid eye colors listed
	"""

	validcolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return str in validcolors

def PassportIDTest(pid):
	"""
	takes in the string of passport number
	checks length (if < 9 or > 9, not valid)
	then check content (are all characters numbers)
	"""
	if len(pid) == 9:
		if pid.isdigit():
			return True
	return False

def ParsePassport(arr):
	"""
	This function takes in the complete 7-8 field length array,
	and parses it into pieces to be passed back out
	"""
	# initialize new array for values to be copied to
	parsed_arr = []
	for p in arr:
		parsed_arr.append(p[4:])
	return parsed_arr

def RemoveCID(arr):
	"""
	This function takes in an array of length 8,
	and removes the second entry (corresponds to
	'cid' field)
	"""
	arr.pop(1)
	return arr

def FinalTest(arr):
	"""
	this function calls all of the
	tests on the passed in passport entry,
	multiplies these results together
	returns 1 if all tests passed
	returns 0 if any test fails
	NOTE: there should be no 'cid' field,
	as we are ignoring this field
	"""

	# first, call a function that will remove the 'cid'
	# field from any of the passed in passports with length of 8
	l = len(arr)
	if l == 8:
		arr = RemoveCID(arr)

	# initialize results array
	results = []

	# save the data as names for ease of reading
	# for numeric entries, first check if is numeric
	# if not, return false

	if arr[0].isdigit():
		byr = int(arr[0])
	else:
		return False
	
	ecl = arr[1]
	
	if arr[2].isdigit():
		eyr = int(arr[2])
	else:
		return False

	hcl = arr[3]
	
	hgt = arr[4]
	
	if arr[5].isdigit():
		iyr =int( arr[5])
	else:
		return False
	
	pid = arr[6]

	# get results and append to results array
	results.append(NumberTest(byr,1920,2002))
	results.append(EyeColorTest(ecl))
	results.append(NumberTest(eyr, 2020, 2030))
	results.append(HairColorTest(hcl))
	results.append(HeightTest(hgt))
	results.append(NumberTest(iyr, 2010, 2020))
	results.append(PassportIDTest(pid))

	# initialize r as 1 to be multiplied by results
	r = 1
	for res in results:
		r *= res

	return r

# initialize empty list to hold cleaned passport entries
clp = []

for p in passports:
	clp.append(CleanUpEntry(p))

# get the total number of passports
totalpassports = len(clp)

# initialize variable to count number of valid passports
validcount = 0

firstvalidcheck = []

# loop over cleaned passports array and push the valid ones
# to firstvalidcheck
for c in clp:
	if LengthTest(c):
		firstvalidcheck.append(c)

# now, the only entries in firstvalidcheck should have either
# length of 7, missing 'cid' field only, and sorted alphabetically
# order is as follows: len(8)  len(7)
#  ['byr:1931',			p[0]	p[0]
# 	'cid:128',			p[1] 	
# 	'ecl:amb',			p[2]	p[1]
# 	'eyr:2029',			p[3]	p[2]
# 	'hcl:z',			p[4]	p[3]
# 	'hgt:150cm',		p[5]	p[4]
# 	'iyr:2015',			p[6]	p[5]
# 	'pid:148714704']	p[7]	p[6]

# pass the entries of firstvalidcheck first to parse the values
for idx, val in enumerate(firstvalidcheck):
	firstvalidcheck[idx] = ParsePassport(val)

# initialize finalvalidationcount variable
finalvalidationcount = 0

# now pass the parsed pieces of code to the FinalTest function
for parsed in firstvalidcheck:
	result = FinalTest(parsed)

	if result == 1:
		finalvalidationcount += 1


print('According to these rules, there are ' + str(finalvalidationcount) \
	+ ' valid passports in this batch, ' \
	+ 'out of ' + str(totalpassports) + ' total.')