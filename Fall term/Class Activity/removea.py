a = ["Aaron", "Albert", "Asheley", "George"]
x = 0
b = 0
for b in range(3):
	if "A" in a[x]:
		del a[x]
print(a)