def answer(x):
	# your code here
	if(x == 0):
		return []
	ret = []
	while(x >= 2):
		mod = int(x % 3)
		if(mod == 0):
			ret.append('-')
		elif(mod == 1):
			ret.append('R')
		elif(mod == 2):
			ret.append('L')
		x = int(round(x / 3.0))
	ret.append('R')
	return ret

print(answer(int(input())))