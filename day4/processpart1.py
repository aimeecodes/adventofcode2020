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
	ecl 	[Eye Color]
	pid 	[Passport ID]
	cid 	[Country ID]
	"""
	str = str.replace('\n', ' ')

	# split the cleaned string into an array 
	arr = str.split()

	# rearrange the items in alphabetical order
	arr = sorted(arr)

	return arr

def CheckValidity(arr):
	"""
	# this function will decide if a passport is valid or not
	# Valid == True, Invalid == False
	# first it checks the length of the array:
	# 	length == 8 	> valid
	# 	length == 7 	> passed to another function to see which field
	# 					is missing
	# 	length <= 6 	> not valid
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

# initialize empty list to hold cleaned passport entries
clp = []

for p in passports:
	clp.append(CleanUpEntry(p))

# get the total number of passports
totalpassports = len(clp)

# initialize variable to count number of valid passports
validcount = 0

# loop over cleaned passports array and count the number
# of valid ones
for c in clp:
	if CheckValidity(c):
		validcount +=1

print('According to these rules, there are ' + str(validcount) \
	+ ' valid passports in this batch, ' \
	+ 'out of ' + str(totalpassports) + ' total.')