#Authors SriVennelaVaishnapu 
#Email vennelavaishnapu2003@gmail.com
#Gamma correction Algorithm
#gammaCorrection = 1 / gamma
#colour = GetPixelColour(x, y)
#newRed   = 255 * (Red(colour)   / 255) ^ gammaCorrection
#newGreen = 255 * (Green(colour) / 255) ^ gammaCorrection
#newBlue  = 255 * (Blue(colour)  / 255) ^ gammaCorrection
#PutPixelColour(x, y) = RGB(newRed, newGreen, newBlue)
from PIL import Image
import random
i = Image.open("input.png")
#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size
j=Image.new(i.mode,i.size)
gamma=input("enter the value of gamma range:0.25  to 2.0")
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #gamma value can range from 0.25 to 2.0
      gammaCorrection = 1 / gamma
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      newRed   = int(255 * ((cpixel[0]/ 255.0)**gammaCorrection))
      newGreen = int(255 * ((cpixel[1]/ 255.0)**gammaCorrection))
      newBlue  = int(255 * ((cpixel[2]/ 255.0)**gammaCorrection))
      j.putpixel((x,y),(newRed, newGreen, newBlue))
j.save('output.png')
