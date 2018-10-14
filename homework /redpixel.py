#Leo Li
#10/13/18
#description: this program creates a image full of red pixel by using the image function in the python library.

from PIL import Image

imgx = 512#the width of the image
imgy = 512#the height of the image

image = Image.new("RGB",(imgx,imgy))#create a new image that has a size of imgx, imgy, and uses color mode RGB

for i in range (512):
	for j in range (512):
		image.putpixel((i,j),(255,0,0))#for everypixel in the image, fill in color red.

image.save("image.png", "PNG")#save the image
