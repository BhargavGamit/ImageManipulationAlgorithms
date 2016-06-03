# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# bi toning algorithm
#         blue = 255.0f / blueLevelFloat * (float )pixelBuffer[k]; 
#         green = 255.0f / greenLevelFloat * (float)pixelBuffer[k + 1]; 
#         red = 255.0f / redLevelFloat * (float)pixelBuffer[k + 2]; 
#         if (blue > 255) {blue = 255;}
#         else if (blue < 0) {blue = 0;}
#         if (green > 255) {green = 255;}
#         else if (green < 0) {green = 0;}
#         if (red > 255) {red = 255;}
#         else if (red < 0) {red = 0;}
from PIL import Image
i = Image.open("input.png")

pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)
blueLevelFloat=input("Enter the color level for blue which is ranging from 0 to 255:  ")
greenLevelFloat=input("Enter the color level for green which is ranging from 0 to 255: ")
redLevelFloat=input("Enter the color level for red which is ranging from 0 to 255:   ")
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      outputBlue = int(255.0 / blueLevelFloat * cpixel[0]); 
      outputGreen = int(255.0 / greenLevelFloat * cpixel[1]); 
      outputRed = int(255.0 / redLevelFloat * cpixel[2]); 
      if(outputRed>255):
          outputRed=255
      elif(outputRed<0):
          outputRed=0
      if(outputGreen>255):
          outputGreen=255
      elif(outputGreen<0):
          outputGreen=0
      if(outputBlue>255):
          outputBlue=255
      elif(outputBlue<0):
          outputBlue=0
      j.putpixel((x,y),(outputRed,outputGreen,outputBlue))
j.save('output.png')

