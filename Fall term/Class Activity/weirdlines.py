from PIL import Image
import random

imgx=512
imgy=512

image = Image.new("RGB", (imgx,imgy))


for i in range(100):
	x = random.randint(0,511)
	b = random.randint(0,255)
	c = random.randint(0,255)
	d = random.randint(0,255)
	for j in range(511):
		a = random.randint(-1,1)
		if x>=0 and x<=511:
			image.putpixel((x,j),(b,c,d))
			x+=a
			print(i,j,x)

image.save("image3.png", "PNG")




