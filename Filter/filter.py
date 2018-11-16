#Leo Li
#11/16/2018
#Description: This is the sobel filter. It traces out the edge of an image and blacks out everything else
#source:http://homepages.inf.ed.ac.uk/rbf/HIPR2/sobel.htm



from PIL import Image
import sys
import math

def main():
	global img,j,w
	img = Image.open(sys.argv[1])#using the commandline argument to open the file
	w,h = img.size
	newimg = Image.new("RGB", (w,h), "white")
	for j in range(1, w-1):#for every single pixel in the picture(except the corners)
		for i in range(1, h-1):
			Gx = 0
			Gy = 0#add values of gradients to each pixel around it according to the kernel
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

			l = math.sqrt(Gx**2+Gy**2)#calculate the length
			l = int(l/w*255)#scale the image
			newimg.putpixel((j,i),(l,l,l))
			percentage()
	
	newimg.show()
	newimg.save("Image1.png", "PNG")

def takepixels(a, b):
	global img,x
	pixel = img.getpixel((a,b))
	r = pixel[0]
	g = pixel[1]
	b = pixel[2]
	x = r+g+b

#it shows the percentage of the program since sometimes it takes a long time for the program to process
def percentage():
	p = j/w*100
	print(str(p)+"%")
	


main()