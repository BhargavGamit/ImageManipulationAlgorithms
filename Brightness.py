# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Brightness algorithm
# colour = GetPixelColour(x, y)
# newRed   = Truncate(Red(colour)   + brightness)
# newGreen = Truncate(Green(colour) + brightness)
# newBlue  = Truncate(Blue(colour)  + brightness)
# PutPixelColour(x, y) = RGB(newRed, newGreen, newBlue)
# Procedure Truncate(value)
#   If value < 0 Then value = 0
#   If value > 255 Then value = 255
#   Return value
#  EndProcedure

from PIL import Image
i = Image.open("input.png")

pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)
def Truncate(value):
   if(value < 0):
     value = 0
   if(value > 255):
     value = 255
   return value
   
brightness=input("Enter value to increase brightness int value")

for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y] 
      j.putpixel((x,y),(Truncate(cpixel[0] + brightness),Truncate(cpixel[1] + brightness),Truncate(cpixel[2] + brightness)))
j.save('output.png')
