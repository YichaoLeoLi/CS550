def countx(str):
	global n,m
	n = 0
	m = 0
	while n<len(str):
		if str[n]=='x':
			m+=1
		n+=1
	return m

b = input("enter a string:")
print(countx(b))