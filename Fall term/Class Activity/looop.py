while True:
	try:
		num = int(input("pick a number between 1 and 5\n>>"))
		while num<1 or num>5:
			num = int(input("I don't take that, please re-enter a number between 1 and 5:\n>>"))
		print("sucess!")
		break
	except ValueError:
		print("That's not a number, please try again")



