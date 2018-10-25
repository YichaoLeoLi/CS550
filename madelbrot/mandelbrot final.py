#Leo Li
#10/25/18
#Mandelbrot set images
#Description: the program generates three different images; the first two are different zooms of the mandelbrot set using different colors. The third one is a Julia set using a another coloring method.
#Honor Code: I have neither given nor received any unauthorized aid.
#Sources: https://www.mcgoodwin.net/julia/juliajewels.html
#https://www.atopon.org/mandel/#
#https://en.wikipedia.org/wiki/Julia_set




from PIL import Image
import random


def mandel1():# the first picture

	xa, xb =0.2501640625, 0.30640625
	ya, yb =-0.0339453125, 0.039296875
#above is the range of the picture
	imgx, imgy = 512, 512
#the size of the picture
	maxIt = 256#max iteration number is 256 since there are only 255 numbers in RGB scale
	image = Image.new('RGB', (imgx,imgy))

	for y in range (imgy):
		cy = y*(yb-ya)/(imgy-1)+ya#cut the image into small pieces, and get the y coordinate of the point 
		for x in range (imgx):
			cx = x*(xb-xa)/(imgx-1)+xa#get the x coordinate of the point
			c = complex(cx,cy)#c corresponds to cx and cy; since c is a complex number, we use the complex() command
			z=0#z is 0 at first
			for i in range(maxIt):
				if abs(z)>=2.0:
					break#the process repeats until the absolute value of z is greater than or equal to 2
				z = z**2 + c#the formula of mandelbrot set


			r = 0
			g = 100+(-15*i)%175#This algorithm draws a gradient of color, and I mod it by 175 to restrict its period
			b = 100+(-10*i)%175
			image.putpixel((x,y),(r,g,b))

	image.show()


def mandel2():

	xa, xb =-0.5749397277832031, -0.5506839752
	ya, yb =-0.65574645, -0.6314907

	imgx, imgy = 512, 512

	maxIt = 256
	image = Image.new('RGB', (imgx,imgy))

	for y in range (imgy):
		cy = y*(yb-ya)/(imgy-1)+ya
		for x in range (imgx):
			cx = x*(xb-xa)/(imgx-1)+xa
			c = complex(cx,cy)
			z=0
			for i in range(maxIt):
				if abs(z)>=2.0:
					break
				z = z**2 + c


			r = 100+(25*i)%50#In this one, I used 25*i to make the value comparatively large, but modding it by 50 can make it cycle really fast. Therefore, color blocks that are close to each other may have different colors, but blocks that have another block between them can have similar colors. The original picture looks like a snowflake, but doing this make the snowflake not that obvious; instead, the picture looks like five pillars.
			g = 100+(20*i)%50
			b = 0
			image.putpixel((x,y),(r,g,b))

	image.show()

def Julia():

	xa, xb =-1, 1
	ya, yb =-1, 1

	imgx, imgy = 512, 512



	maxIt = 256
	img = Image.new('RGB', (imgx,imgy), "white")

	for y in range (1, imgy-1):
		cy = y*(yb-ya)/(imgy-1)+ya
		for x in range (1, imgx-1):
			cx = x*(xb-xa)/(imgx-1)+xa
			c = complex(0.6, 0.55)#in Julia set, c is a constant
			z = complex(cx, cy)#z is dependent on the coordinate
			for i in range(maxIt):
				if abs(z)>=2.0:
					break
				z = z**4+c#formula for this specific Julia set

			a = random.randint(0,2)
			b = random.randint(0,50)
				

			if i <= 20:#For anything other thant the central piece of the Julia set, the rgb value of each pixel is 20*a, a random number between 0 and 1. This creates noise in areas other than the central piece, which I think is cool.
				r = 20*a
				g = 20*a
				b = 20*a

			else: #I made these choices because in this way the picture looks golden, which is cool. I added b also to create some slight noises in the picture
				r = 20*i+-b
				g = 10*i+-b
				b = 5*i+-b
			img.putpixel((x,y),(r,g,b))





	img.show()




mandel1()
mandel2()
Julia()