#Author SriVennelaVaishnapu 
#Email vennelavaishnapu2003@gmail.com
#Contrast Algorithm
#factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
#colour = GetPixelColour(x, y)
#newRed   = Truncate(factor * (Red(colour)   - 128) + 128)
#newGreen = Truncate(factor * (Green(colour) - 128) + 128)
#newBlue  = Truncate(factor * (Blue(colour)  - 128) + 128)
#PutPixelColour(x, y) = RGB(newRed, newGreen, newBlue)
#Procedure Truncate(value)
#   If value < 0 Then value = 0
#   If value > 255 Then value = 255
#   Return value
#EndProcedure
from PIL import Image
i = Image.open("input.png")
#debugging purpose
#print(i.format,i.size,i.mode)
#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size
j=Image.new(i.mode,i.size)
contrast=input("enter contrast value range:-255 to 255")
def Truncate(value):
   if(value < 0):
     value = 0
   if(value > 255):
     value = 255
   return value
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y] 
      factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      newRed   = Truncate((factor * (cpixel[0] - 128) + 128))
      newGreen = Truncate((factor * (cpixel[1] - 128) + 128))
      newBlue  = Truncate((factor * (cpixel[2] - 128) + 128))
      j.putpixel((x,y),(newRed, newGreen, newBlue))
j.save('output.png')
