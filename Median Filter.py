# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Median filter

from PIL import Image
i = Image.open("input.jpg")

#pixel data is stored in pixels in form of two dimensional array
pixels = i.load()
width, height = i.size
k=Image.new(i.mode,i.size)

filtersize=input('Enter the size of the filter: ')
filterOffset=(filtersize-1)/2
filterheight=filtersize
filterwidth=filtersize
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
        if(x>=offsetx and y>=offsety and x < width and y <height):
            cpixel=pixels[x-offsetx,y-offsety]
            j.putpixel((x,y),cpixel)

for y in range(height+(2*offsety)):
    for x in range(width+(2*offsetx)):
        if(x>=offsetx and y>=offsety and x < width and y <height):
            blue=0.0
            green=0.0
            red=0.0
            blues=list()
            reds=list()
            greens=list()
            filterx=x-offsetx
            filtery=y-offsety
            for fy in range(filterheight):
                for fx in range(filterwidth):
                    cpixel=j.getpixel((x-offsety+fx,y-offsety+fy))
                    reds.append(float(cpixel[0]))
                    greens.append(float(cpixel[1]))
                    blues.append(float(cpixel[2]))
            reds.sort()
            blues.sort()
            greens.sort()
            index=len(reds)
            medianindex=index/2
            if(index%2!=0):
                red=reds[medianindex]
                blue=blues[medianindex]
                green=greens[medianindex]
            else:
                red=(reds[medianindex]+reds[medianindex+1])/2
                blue=(blues[medianindex]+blues[medianindex+1])/2
                green=(greens[medianindex]+greens[medianindex+1])/2
            k.putpixel((x-offsetx,y-offsety),(int(red),int(green),int(blue)))
            del reds[:]
            del blues[:]
            del greens[:]
k.save('output.png')
