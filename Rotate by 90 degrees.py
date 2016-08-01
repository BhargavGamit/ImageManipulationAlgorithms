# Author Kavya S
# Email kavyareddy357@gmail.com
# Rotate image by 90 degrees

from PIL import Image
i = Image.open("input.jpg")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load()
width, height = i.size
j=Image.new(i.mode,(height,width))


#cpixel[0] contains red value   cpixel[1] contains green value
#cpixel[2] contains blue value  cpixel[3] contains alpha value
for image_width_iterator in range(width):
    for image_height_iterator in range(height):
        cpixel = pixels[image_width_iterator,image_height_iterator]
        j.putpixel((abs(height-1-image_height_iterator),abs(image_width_iterator)),(cpixel))
j.save('output.png')
