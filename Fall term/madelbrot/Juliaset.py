from PIL import Image


def Julia():

	xa, xb =-2, 2
	ya, yb =-2, 2

	imgx, imgy = 512, 512

	maxIt = 256
	image = Image.new('RGB', (imgx,imgy))

	for y in range (imgy):
		cy = y*(yb-ya)/(imgy-1)+ya
		for x in range (imgx):
			cx = x*(xb-xa)/(imgx-1)+xa
			c = complex(-0.7269, 0.1889)
			z = complex(cx, cy)
			for i in range(maxIt):
				if abs(z)>=2.0:
					break
				z = z**2+c


			r = 0
			g = 0
			b = i
			image.putpixel((x,y),(r,g,b))

	image.show()