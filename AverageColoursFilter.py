# Author Bhargav K
# Email bhargav.gamit@gmail.com
# AverageColoursFilter


from PIL import Image
i = Image.open("input.png")

#store pixels of input image
pixels = i.load()
width, height = i.size
k=Image.new(i.mode,i.size)

print "Filter size should be an odd positive number"
filtersize=input("Choose the Size of Filter: ")
print "Type (True) or (False) without braces"
applyred=input  ("Choose to apply red   : ")
applygreen=input("Choose to apply green : ")
applyblue=input ("Choose to apply blue  : ")
print "Choose Shift Type"
print "1 None "
print "2 Shift Left"
print "3 Shift Right"
shifttype=input()
filterwidth=filtersize
filterheight=filtersize

filterOffset = (filterwidth-1)/2;

offsety=filterOffset
offsetx=filterOffset


j = Image.new(i.mode,(width+(2*offsetx),height+(2*offsety)))

for x in range(width+(2*offsetx)):
    for y in range(height+(2*offsety)):
        if(x<offsetx):
            j.putpixel((x,y),(0,0,0))
        if(y<offsety):
            j.putpixel((x,y),(0,0,0))
        if(x>=width):
            j.putpixel((x,y),(0,0,0))
        if(y>=height):
            j.putpixel((x,y),(0,0,0))
        if(x>=offsetx and y>=offsety and x <=width and y <=height):
            cpixel=pixels[x-offsetx,y-offsety]
            j.putpixel((x,y),cpixel)


for y in range(height+(2*offsety)):
    for x in range(width+(2*offsetx)):
        if(x>=offsetx and y>=offsety and x <=width and y <=height):
            blue=0.0
            green=0.0
            red=0.0
            filterx=x-offsetx
            filtery=y-offsety
            for fy in range(filterheight):
                for fx in range(filterwidth):
                    cpixel=j.getpixel((x-offsety+fx,y-offsety+fy))
                    red+=float(cpixel[0])
                    green+=float(cpixel[1])
                    blue+=float(cpixel[2])
            red=red/filtersize
            green=green/filtersize
            blue=blue/filtersize
            cpixel=j.getpixel((x,y))
            if(applyred==False):
                red=cpixel[0]
            if(applygreen==False):
                green=cpixel[1]
            if(applyblue==False):
                blue=cpixel[2]
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
            if(shifttype==1):
                k.putpixel((x-offsetx,y-offsety),(int(red),int(green),int(blue)))
            if(shifttype==2):
                k.putpixel((x-offsetx,y-offsety),(int(blue),int(red),int(green)))
            if(shifttype==3):
                k.putpixel((x-offsetx,y-offsety),(int(green),int(blue),int(red)))
k.save('output.png')
