# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Bitwise Blending 
# AND OR XOR
# AND color=firstimagecolor & secondimagecolor
# OR  color=firstimagecolor | secondimagecolor
# XOR color=firstimagecolor ^ secondimagecolor

from PIL import Image
i = Image.open("input1.png")
j = Image.open("input2.png")

#store pixels of first image
pixels_first = i.load()
width_first, height_first = i.size
k=Image.new(i.mode,i.size)

#store pixels of second image
pixels_second = j.load()
width_second,height_second = j.size


blue=0
green=0
red=0

print "Choose Bitwise blendtypes as follows"
print "1 AND \n2 OR \n3 XOR\n"

redblend=input("Choose red blend type")
greenblend=input("Choose green blend type ")
blueblend=input("Choose blue blend type ")

#cpixel[0] contains red value   cpixel[1] contains green value
#cpixel[2] contains blue value  cpixel[3] contains alpha value
for image_width_iterator in range(width_first):
    for image_height_iterator in range(height_first):
        cpixel = pixels_first[image_width_iterator, image_height_iterator]
        dpixel = pixels_second[image_width_iterator,image_height_iterator]
        if(redblend == 1):
            red=cpixel[0]&dpixel[0]
        elif(redblend == 2):
            red=cpixel[0]|dpixel[0]
        elif(redblend==3):
            red=cpixel[0]^dpixel[0]
        else:
            red=0
        if(greenblend == 1):
            green=cpixel[1]&dpixel[1]
        elif(greenblend == 2):
            green=cpixel[1]|dpixel[1]
        elif(greenblend==3):
            green=cpixel[1]^dpixel[1]
        else:
            blue=0
        if(blueblend == 1):
            blue=cpixel[2]&dpixel[2]
        elif(blueblend == 2):
            blue=cpixel[2]|dpixel[2]
        elif(blueblend==3):
            blue=cpixel[2]^dpixel[2]
        else:
            blue=0
        if(red<0):
            red=0
        if(red>255):
            red=255
        if(green<0):
            green=0
        if(green>255):
            green=255
        if(blue<0):
            blue=0
        if(blue>255):
            blue=255
        k.putpixel((image_width_iterator,image_height_iterator),(red,green,blue))
k.save('output.png')
