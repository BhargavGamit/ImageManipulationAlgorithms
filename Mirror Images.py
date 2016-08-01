# Author Kavya S, Bhargav K
# Email kavyareddy357@gmail.com, bhargav.gamit@gmail.com
# Mirroring Image

from PIL import Image
i = Image.open("input.jpg")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load()
width, height = i.size
j=Image.new(i.mode,i.size)

print "1 Mirror along X and Y axis"
print "2 Mirror along Y axis"
print "3 Mirror along X axis"

option=input('Enter your choice: ')
if option == 1:
    widthmodifier=width-1
    heightmodifier=height-1
elif option == 2:
    widthmodifier=0
    heightmodifier=height-1
else:
    widthmodifier=width-1
    heightmodifier=0

for image_width_iterator in range(width):
    for image_height_iterator in range(height):
        cpixel = pixels[image_width_iterator,image_height_iterator]
        j.putpixel((abs(widthmodifier-image_width_iterator),abs(heightmodifier-image_height_iterator)),(cpixel))
j.save('output.png')
