#!/usr/bin/env python3
from PIL import Image, ImageDraw
import sys

image=Image.open(sys.argv[1])
txt=sys.argv[2]
width = image.size[0]
height = image.size[1]
draw = ImageDraw.Draw(image)

buff=""
for c in txt:
	tmp=bin(ord(c))[2:]
	tmp=(8-len(tmp))*'0'+tmp
	buff+=tmp

ind=-1

pix = image.load()
for i in range(width):
	for j in range(height):
		R = pix[i, j][0]
		G = pix[i, j][1]
		B = pix[i, j][2]
		ind+=1
		if(ind>len(buff)):
			image.save("encrypted-"+sys.argv[1])
			print("Wrote")
			sys.exit(0)
		elif(ind==len(buff)):
			if(R%2==G%2):
				R+=1
				if(R==256):R=254
		else:
			cur=buff[ind]
			R+=R%2
			if(R>255):R=254
			G+=G%2
			if(G>255):G=254
			B+=B%2
			if(B>255):B=254
			if(cur=='1'):
				R+=1
				G+=1
				B+=1
		draw.point((i, j), (R, G, B))
