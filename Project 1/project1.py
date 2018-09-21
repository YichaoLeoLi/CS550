def start():
	while True:
		try:
			result = int(input("hello"))
			while result < 1 or result > 2:
				result = int(input("Please enter 1 or 2:\n>>"))
				print(result < 1 or result > 2)
			print("success!")
			break
		except ValueError:
			print("That's not an integer, please try again")
def chapter1():




start()
chapter1()