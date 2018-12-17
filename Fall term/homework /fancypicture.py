#Leo Li
#10/13/18
#Description: this program creates a image with fancy colors; the color that the program fills in depends on the location of the pixel

from PIL import Image

imgx = 512#width of the image
imgy = 512#height of the image

image = Image.new("RGB",(imgx,imgy))#create a new image with size imgx, imgy, and color mode RGB

for i in range (512):
	for j in range (512):
		image.putpixel((i,j),(i%255,j%255,(i+j)%255))#for every pixel in the image, its color is equal to (i%255, j%255, (i+j)%255), where i is the x location of the pixel and j is the y location of the pixel

image.save("image1.png", "PNG")#save the image
