#Leo Li
#09/27/18
#Description: task for this program is Take two values, base and exponent, from the user. Then create a list that displays the exponents of that base from the 0 power (1) to the [entered exponent] power in ascending order. For example, if the base was 2 and the exponent was 5, the list should show [1, 2, 4, 8, 16, 32] 
import math
a = []
x = float(input("\nplease enter the base\n\n>>"))
y = float(input("\nplease enter the exponent\n\n>>"))
z = 0
while z<(y+1):#when z is smaller then the exponent, keep adding terms
	a.append(x**z)
	z+=1
print("\n",a)