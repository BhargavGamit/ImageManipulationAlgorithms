# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# ColourTint algorithm
#blue = pixelBuffer[k] + (255 - pixelBuffer[k]) * blueTint; 
#         green = pixelBuffer[k + 1] + (255 - pixelBuffer[k + 1]) * greenTint; 
#         red = pixelBuffer[k + 2] + (255 - pixelBuffer[k + 2]) * redTint; 
#        if (blue > 255) 
#        { blue = 255; } 
#        if (green > 255) 
#        { green = 255; } 
#        if (red > 255) 
#        { red = 255; } 

from PIL import Image
i = Image.open("input.png")
print(i.format,i.size,i.mode)
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)
blueTint=input("enter the percentage of blue tint in fraction") 
greenTint=input("enter the percentage of green tint in fraction")
redTint=input("enter the percentage of red tint in fraction") 
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      outputBlue = int(cpixel[0] + (255 - cpixel[0]) * blueTint); 
      outputGreen = int(cpixel[1]  + (255 - cpixel[1]) * greenTint); 
      outputRed =  int(cpixel[2] + (255 -  cpixel[2]) * redTint); 
      if(outputRed>255):
          outputRed=255
      if(outputGreen>255):
          outputGreen=255
      if(outputBlue>255):
          outputBlue=255
      j.putpixel((x,y),(outputRed,outputGreen,outputBlue))
j.save('output.png')

