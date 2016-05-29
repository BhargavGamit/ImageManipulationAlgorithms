# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Luminance algorithm
# luma = (red*0.3+green*0.59+blue*0.11)

from PIL import Image
i = Image.open("input.png")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load() 
width, height = i.size
j=Image.new(i.mode,i.size)

#cpixel[0] contains red value   cpixel[1] contains green value
#cpixel[2] contains blue value  cpixel[3] contains alpha value
for image_width_iterator in range(width):
    for image_height_iterator in range(height):
        cpixel = pixels[image_width_iterator, image_height_iterator]
        luma = int((cpixel[0]*0.3)+(cpixel[1]*0.59)+(cpixel[2]*0.11))
        j.putpixel((image_width_iterator,image_height_iterator),(luma,luma,luma))
j.save('output.png')


