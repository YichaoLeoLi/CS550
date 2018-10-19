def function():
	x = 0
	y = 0
	c = 0
	a = float(input("\nPlease enter the x coordinate of c\n>>"))
	b = float(input("\nPlease enter the y coordinate of c\n>>"))
	for c in range (10):
		
		x = x**2-y**2+a
		y = 2*x*y+b
		if (x**2+y**2)**0.5>=2:
			print(c+1)			
			break
		elif c>=2:
			print(c+1)
			break

while True:
	function()
