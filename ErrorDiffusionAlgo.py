#Authors Bhargav K,SriVennelaVaishnapu 
#Email vennelavaishnapu2003@gmail.com
#Error Diffusion Algorithm
#error = actualColour - nearestColour
#PutPixelColour(x+1, y  ) = Truncate(GetPixelColour(x+1, y  ) + 0.5 * error)
#PutPixelColour(x  , y+1) = Truncate(GetPixelColour(x  , y+1) + 0.5 * error)
#Procedure Truncate(value)
#   If value < 0 Then value = 0
#   If value > 255 Then value = 255
#   Return value
#EndProcedure

from PIL import Image
i = Image.open("lena.jpg")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load()
width, height = i.size
j=Image.new(i.mode,i.size)
def Truncate(value):
   if(value < 0):
     value = 0
   if(value > 255):
     value = 255
   return value
def Error(value):
   if(value >= 0  and value <=127):
      return 0
   else:
      return 128
for x in range(width-1):
    for y in range(height-1):
      cpixel = pixels[x, y]
      #cpixel[0] contains red value   cpixel[1] contains green value
      #cpixel[2] contains blue value  cpixel[3] contains alpha value
      error_red = cpixel[0]-Error(cpixel[0])
      error_green = cpixel[1]-Error(cpixel[1])
      error_blue = cpixel[2]-Error(cpixel[2])
      apixel= pixels[x+1,y]
      bpixel= pixels[x,y+1]
      j.putpixel((x+1, y  ),(int(Truncate(apixel[0] + 0.5 * error_red)),int(Truncate(apixel[1]+0.5*error_blue)),int(Truncate(apixel[2]+0.5*error_green))))
      j.putpixel((x  , y+1),(int(Truncate(bpixel[0] + 0.5 * error_red)),int(Truncate(bpixel[1]+0.5*error_blue)),int(Truncate(bpixel[2]+0.5*error_green))))

j.save('error.png')
