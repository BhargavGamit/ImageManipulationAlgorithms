# Author Sri Vennela Vaishnapu
# Email vennelavaishnapu2003@gmail.com
# Bitonal algorithm
#if  (pixelBuffer[k] + pixelBuffer[k + 1] +  
#             pixelBuffer[k + 2] <= threshold) 
#        { 
#            pixelBuffer[k] = darkColor.B; 
#            pixelBuffer[k + 1] = darkColor.G; 
#            pixelBuffer[k + 2] = darkColor.R; 
#        } 
#        else  
#        { 
#            pixelBuffer[k] = lightColor.B; 
#            pixelBuffer[k + 1] = lightColor.G; 
#            pixelBuffer[k + 2] = lightColor.R; 
#        }
from PIL import Image

print "Enter values between 0 and 255"
lightcolor_red=input("Enter red value of light color:   ")
lightcolor_blue=input("Enter blue value of light color:  ")
lightcolor_green=input("Enter green value of light color: ")
darkcolor_red=input("Enter red value of dark color:    ")
darkcolor_blue=input("Enter blue value of dark color:   ")
darkcolor_green=input("Enter green value of dark color:  ")
i = Image.open("input.png")
#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)
threshold = 374
for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      if(int(cpixel[0] + cpixel[1] +cpixel[2]) > int(threshold)): 
         red = lightcolor_red  
         green = lightcolor_green 
         blue = lightcolor_blue
         j.putpixel((x,y),(red,green,blue))
      else:  
         red = darkcolor_red
         green = darkcolor_green
         blue = darkcolor_blue
         j.putpixel((x,y),(red,green,blue))
j.save('output.png')
