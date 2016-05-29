#Author SriVennela Vaishnapu
#Email vennelavaishnapu2003@gmail.com
#Desaturation Algorithm
#Gray = ( Max(Red, Green, Blue) + Min(Red, Green, Blue) ) / 2

from PIL import Image
import math
import random
i = Image.open("input.png")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)

 #loop for storing each pixel of original image in new variable cpixel   
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] is for red value cpixel[1] is for green value cpixel[2] is for blue value
      Gray = int( max(cpixel[0],cpixel[1],cpixel[2]) +min(cpixel[0],cpixel[1],cpixel[2]) ) / 2
      j.putpixel((x,y),(Gray,Gray,Gray))
j.save('output.png')
