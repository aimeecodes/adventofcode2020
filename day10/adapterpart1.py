inputfile = './input.txt'

with open(inputfile) as f:
	lines = [line.rstrip('\n') for line in f]