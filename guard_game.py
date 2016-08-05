def answer(x):
	# your code here
	if(x < 10):
		return x
	ret = 0
	for i in str(x):
		ret += int(i)
	return answer(ret)

print(answer(int(input())))