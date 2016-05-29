# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Single Color Channel using red
# gray = red

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
        gray = cpixel[0]
        j.putpixel((image_width_iterator,image_height_iterator),(gray,gray,gray))
j.save('output.png')


