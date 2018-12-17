from PIL import Image

imgx = int(input("\nPlease enter the width of the image\n>>"))
imgy = int(input("\nPlease enter the height of the image\n>>"))
a = int(input("\nPlease enter the number of rows you want\n>>"))
b = int(input("\nPlease enter the number of columns you want\n>>"))
image = Image.new("RGB", (imgx, imgy))
c = imgx/b
d = imgy/a
x = 0
y = 0

for y in range(imgy):
	for x in range(imgx):
		if y%(2*d)<=d:
			if x%(2*c)<=c:
				image.putpixel((x,y),(0,0,0))
			elif x%(2*c)<(2*c):
				image.putpixel((x,y),(255,0,0))
		elif y%(2*d)<(2*d):
			if x%(2*c)<=c:
				image.putpixel((x,y),(255,0,0))
			elif x%(2*c)<(2*c):
				image.putpixel((x,y),(0,0,0))

image.save('image4.png', "PNG")