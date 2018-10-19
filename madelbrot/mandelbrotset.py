from PIL import Image 
import math as k


def set():
	global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c, a, b, e, f
	c1 = k.floor(512/17)
	c2 = k.floor(1024/17)
	c3 = k.floor(1536/17)
	c4 = k.floor(2048/17)
	c5 = k.floor(2560/17)
	c6 = k.floor(3072/17)
	c7 = k.floor(3584/17)
	c8 = k.floor(4096/17)
	c9 = k.floor(4608/17)
	c10 = k.floor(5120/17)
	c11 = k.floor(5632/17)
	c12 = k.floor(6144/17)
	c13 = k.floor(6656/17)
	c14 = k.floor(7168/17)
	c15 = k.floor(7680/17)
	c16 = k.floor(8192/17)
	c17 = k.floor(512)
	for i in range(512):
		for j in range(512):
			a = -2+j/128
			b = 2-i/128
			m=0
			e=0
			f=0
			while True:
				e = e**2+f**2+a
				f = 2*e*f+b
				m+=1
				if m >=16 or (e**2+f**2>=4):
					break
			if m >=16:
				c = c17

			if (e**2+f**2>=4):
				if m ==0:
					c=c1
				elif m == 1:
					c=c2
				elif m == 2:
					c=c3
				elif m == 3:
					c=c4
				elif m == 4:
					c=c5
				elif m == 5:
					c=c6
				elif m == 6:
					c=c7
				elif m == 7:
					c=c8
				elif m == 8:
					c=c9
				elif m == 9:
					c=c10
				elif m ==10:
					c=c11
				elif m == 11:
					c=c12
				elif m == 12:
					c=c13
				elif m == 13:
					c=c14
				elif m == 14:
					c=c15
				elif m == 15:
					c=c16
			image.putpixel((i,j),(c,0,0))
			print (i,j, m)
			print(a,b)




imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
set()
image.save('madelbrot1.png', "PNG")