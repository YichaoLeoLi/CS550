



class Account:
	def __init__(self):
		self.balance = 0
		self.accountnumber = 1234567890123456
		self.pin = 000000
		self.open = False
	def deposit(self, a):
		if a <=20000 and a>0:
			self.balance+=a
			return self.balance
		else:
			error = "\nSorry, you cannot make a deposit that's more than $20000. Please re-enter the amount of money you would like to deposit\n>>"
			return error
			deposit(float(input("\nPlease enter the amount of money you want to deposit\n>>")))
	def withdrawl(self, b):
		if b <= 20000 and b > 0:
			self.balance-=b
			return self.balance
		else:
			error = "\nSorry, you cannot withdraw more than $20000. Please re-enter the amount of money you want to withdraw"
			return error
			withdrawl(float(input("\nPlease enter the amount of money you would like to withdraw\n>>")))


def create():
	x = int(input("\nDo you want to open an account?\n1)Yes\n2)No\n>>"))
	if x == 1:
		account1 = Account()
		account1.open != account1.open
		print("\nYour account number is " + account1.accountnumber)
		y = int(input("\nWould you like to set a pin number?(Your default pin number is 000000)\n1)Yes\n2)No\n>>"))
		if y == 1:
			account1.pin = int.input("\nPlease enter your pin\n>>")
		if y == 2:
			sthelse()

def sthelse():
	z = int(input("\nWould you like to do something else?\n1)Yes\n2)No\n>>"))
			if z == 1:
				choice = int(input("\nWhat would you like to do? \n1)Make a deposit\n2)withdraw\n3)check balance\n4)transfer\n>>"))
				if choice == 1:
					depositt()
				elif choice == 2:
					withdrawll()
				elif choice == 3:
					print(account1.balance)
			if z == 2:
				print("\nThank you for using the service, have a great day!")\
				quit()

def depositt():
	print("deposit successfully made! " + account1.deposit(float(input("\nPlease enter the amount of money you want to deposit\n>>"))))

def withdrawll():
	print(account1.withdrawl(float(input("\nPlease enter the amount of money you would like to withdraw\n>>"))))















