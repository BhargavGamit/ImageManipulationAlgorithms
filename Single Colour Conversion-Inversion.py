# Author Kavya S
# Email kavyareddy357@gmail.com
# Single Color Inversion

from PIL import Image
i = Image.open("input.jpg")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load()
width, height = i.size
j=Image.new(i.mode,i.size)


print '1 Red filter'
print '2 Blue filter'
print '3 Green filter'
print '4 Red Invert filter'
print '5 Blue Invert filter'
print '6 Green Invert filter'
red = 0
blue = 0
green = 0

#cpixel[0] contains red value   cpixel[1] contains green value
#cpixel[2] contains blue value  cpixel[3] contains alpha value
option=input('Enter your choice: ')
for image_width_iterator in range(width):
    for image_height_iterator in range(height):
        cpixel = pixels[image_width_iterator, image_height_iterator]
        if option == 1:
            red = cpixel[0]
        elif option == 2:
            blue = cpixel[2]
        elif option == 3:
            green = cpixel[1];
        elif option == 4:
            red = 255 - cpixel[0]
        elif option == 5:
            blue = 255 - cpixel[2]
        else :
            green = 255 - cpixel[1];
        j.putpixel((image_width_iterator,image_height_iterator),(red,green,blue))
j.save('output.png')
