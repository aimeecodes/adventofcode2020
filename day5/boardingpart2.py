inputfile = './input.txt'

with open(inputfile) as f:
	passes = [line.rstrip('\n') for line in f]

def TranslateToBinary(string, charA, charB, charC, charD):
	"""
	string  	string of characters that
				represent binary code
	char A 		represents power of 2 in first half
	char B 		represents no power of 2 in first half
	char C 		represents power of 2 in last half
	char D 		represents no power of 2 in last half
	"""

	string = string.replace(charA, '1')
	string = string.replace(charB, '0')
	string = string.replace(charC, '1')
	string = string.replace(charD, '0')

	return string

def BinaryToInteger(string, base):
	"""
	A little overkill, but returns the integer
	version of a string specified by base
	"""
	return int(string,base)

def GetSeatID(string):
	return BinaryToInteger(
			TranslateToBinary(
				string,
				'B',
				'F',
				'R',
				'L'),
			2)

# make set of SeatIDs already given
# sets are easier to find differences between
seatset = set()

# initialize max seat ID to 0, and min seat ID to high number
# outside the range of binary number (1111111111)
maxSeatID = 0
minSeatID = 1024

# loop over entries, get SeatID, and update maxSeatID
for p in passes:
	temp = GetSeatID(p)
	seatset.add(temp)

	if temp > maxSeatID:
		maxSeatID = temp

	if temp < minSeatID:
		minSeatID = temp

# create list of numbers that ranges
# from minSeatID to maxSeatID
totalseats = set(range(minSeatID,maxSeatID))

missingSeat = totalseats - seatset

print('Your seat ID should be ' + str(missingSeat) + '.')