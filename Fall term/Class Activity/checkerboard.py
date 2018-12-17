from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

x = 0
y = 0

for y in range(512):
	for x in range(512):
		print(x,y)
		if y%128<=64:
			if x%128<=64:
				image.putpixel((x,y),(0,0,0))
			elif x%128<128:
				image.putpixel((x,y),(255,0,0))
		elif y%128<128:
			if x%128<=64:
				image.putpixel((x,y),(255,0,0))
			elif x%128<128:
				image.putpixel((x,y),(0,0,0))

image.save('image2.png', "PNG")