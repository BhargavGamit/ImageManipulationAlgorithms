# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# Colour Shading algorithm
from PIL import Image
import random 
i = Image.open("lena.jpg")
blueShade =  input("enter the ahdingfactor for blue range:0 to 1")
redShade =  input("enter the ahdingfactor for red range:0 to 1")
greenShade =  input("enter the ahdingfactor for green range:0 to 1")
#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)

for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      blue = int(cpixel[0] * blueShade) 
      green = int(cpixel[1] * greenShade) 
      red = int(cpixel[2] * redShade)
      if(blue < 0): 
           blue = 0  
      if(green < 0): 
           green = 0  
      if(red < 0): 
           red = 0
      j.putpixel((x,y),(red,green,blue))
j.save('shading.png')
