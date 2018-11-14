

from PIL import Image
import sys
import math

def main():
	global img
	img = Image.open(sys.argv[1])
	w,h = img.size
	newimg = Image.new("RGB", (w,h), "white")
	for j in range(1, w-1):
		for i in range(1, h-1):
			print(i,j)
			Gx = 0
			Gy = 0
			takepixels(j-1,i-1)
			Gx+=-x
			Gy+=x
			takepixels(j-1,i)
			Gx+=-2*x
			Gy+=0
			takepixels(j-1,i+1)
			Gx+=-x
			Gy+=-x
			takepixels(j,i-1)
			Gx+=0
			Gy+=2*x
			takepixels(j,i+1)
			Gx+=0
			Gy+=-2*x
			takepixels(j+1,i-1)
			Gx+=x
			Gy+=x
			takepixels(j+1,i)
			Gx+=2*x
			Gy+=0
			takepixels(j+1,i+1)
			Gx+=x
			Gy+=-x

			l = math.sqrt(Gx**2+Gy**2)
			l = int(l/w*255)
			newimg.putpixel((j,i),(l,l,l))
	
	newimg.show()

def takepixels(a, b):
	global img,x
	pixel = img.getpixel((a,b))
	r = pixel[0]
	g = pixel[1]
	b = pixel[2]
	x = r+g+b




main()