# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# Custom algorithm
# ConversionFactor = 255 / (NumberOfShades - 1)
# AverageValue = (Red + Green + Blue) / 3
# Gray = Integer((AverageValue / ConversionFactor) + 0.5) * ConversionFactor

from PIL import Image
import random 
i = Image.open("input.png")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)

#selects the random no of shades between 2 to 256 including 2 and 256
NumberOfShades = int(random.random()*255)+2
ConversionFactor = 255 / (NumberOfShades - 1)
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      AverageValue = (cpixel[0] + cpixel[1] + cpixel[2]) / 3
      gray = int(((AverageValue / ConversionFactor) + 0.5) * ConversionFactor)
      j.putpixel((x,y),(gray,gray,gray))
j.save('output.png')
