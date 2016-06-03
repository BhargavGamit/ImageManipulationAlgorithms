# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# Inversion algorithm
# colour = GetPixelColour(x, y)
# invertedRed   = 255 - Red(colour)
# invertedGreen = 255 - Green(colour)
# invertedBlue  = 255 - Blue(colour)
# PutPixelColour(x, y) = RGB(invertedRed, invertedGreen,invertedBlue)

from PIL import Image
i = Image.open("input.png")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)

for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      invertedRed   = 255 - cpixel[0]
      invertedGreen = 255 - cpixel[1]
      invertedBlue  = 255 - cpixel[2]
      j.putpixel((x, y),(invertedRed, invertedGreen, invertedBlue))
j.save('output.png')
