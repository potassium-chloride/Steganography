#!/usr/bin/env python3
from PIL import Image, ImageDraw
import sys

image=Image.open(sys.argv[1])
width = image.size[0]
height = image.size[1]
s=""
buff=""
pix = image.load()
for i in range(width):
	for j in range(height):
		R = pix[i, j][0]%2
		G = pix[i, j][1]%2
		B = pix[i, j][2]%2
		if(R==G and G==B):
			buff+=str(R)
			if(len(buff)==8):
				s+=chr(int(buff,2))
				buff=""
		else:
			buff=""
			if(len(s)>0):
				print("\""+s+"\"")
				sys.exit(0)

