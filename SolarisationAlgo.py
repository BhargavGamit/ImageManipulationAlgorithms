# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# Solarisation algorithm
# colour = GetPixelColour(x, y)
# If Red(colour) < threshold
#   solariseRed = 255 - Red(colour)
# Else
#   solariseRed = Red(colour)
# EndIf
# If Green(colour) < threshold
#   solariseGreen = 255 - Green(colour)
# Else
#   solariseGreen = Green(colour)
# EndIf
# If Blue(colour) < threshold
#   solariseBlue = 255 - Blue(colour)
# Else
#   solariseBlue = Blue(colour)
# EndIf
# PutPixelColour(x, y) = RGB(solariseRed, solariseGreen, solariseGreen)

from PIL import Image
i = Image.open("input.png")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load()
width, height = i.size
j=Image.new(i.mode,i.size)

threshold=128
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      if(cpixel[0]<threshold):
         solariseRed = 255 - cpixel[0]
      else:
         solariseRed = cpixel[0]

      if(cpixel[1]<threshold):
         solariseGreen = 255 - cpixel[1]
      else:
         solariseGreen = cpixel[1]

      if(cpixel[2]<threshold):
         solariseBlue = 255 - cpixel[2]
      else:
        solariseBlue = cpixel[2]
      j.putpixel((x,y),(solariseRed,solariseBlue,solariseGreen))
j.save('output.png')
