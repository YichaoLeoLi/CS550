from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

for i in range (512):
	for j in range (512):
		image.putpixel((i,j),(255,0,0))

image.save("image.png", "PNG")