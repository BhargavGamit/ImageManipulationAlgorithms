# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Image Convolution


from PIL import Image
i = Image.open("input.png")

#store pixels of input image
pixels = i.load()
width, height = i.size
k=Image.new(i.mode,i.size)


print "1 Blur3x3Filter"
print "2 Blur5x5Filter"
print "3 Gaussian3x3BlurFilter"
print "4 Gaussian5x5BlurFilter"
print "5 SoftenFilter"
print "6 MotionBlurFilter"
print "7 MotionBlurLeftToRightFilter"
print "8 MotionBlurRightToLeftFilter"
print "9 HighPass3x3Filter"
print "10 EdgeDetectionFilter"
print "11 HorizontalEdgeDetectionFilter"
print "12 VerticalEdgeDetectionFilter"
print "13 EdgeDetection45DegreeFilter"
print "14 EdgeDetectionTopLeftBottomRight"
print "15 SharpenFilter"
print "16 Sharpen3x3Filter"
print "17 Sharpen3x3FactorFilter"
print "18 Sharpen5x5Filter"
print "19 IntenseSharpenFilter"
print "20 EmbossFilter"
print "21 Emboss45DegreeFilter"
print "22 EmbossTopLeftBottomRight"
print "23 IntenseEmbossFilter"

userin=input("Choose the Filter: ")

if(userin == 1):
    factor=1.0
    bias=0.0
    filtermatrix=[[0.0,0.2,0.0],[0.2,0.2,0.2],[0.0,0.2,0.2]]
elif(userin == 2):
    factor=1.0/13.0
    bias=0.0
    filtermatrix=[[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
elif(userin == 3):
    factor=1.0/16.0
    bias=0.0
    filtermatrix=[[1,2,1],[2,4,2],[1,2,1]]
elif(userin == 4):
    factor=1.0/159.0
    bias=0.0
    filtermatrix=[[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]]
elif(userin == 5):
    factor=1.0/8.0
    bias=0.0
    filtermatrix=[[1,1,1],[1,1,1],[1,1,1]]
elif(userin == 6):
    factor=1.0/18.0
    bias=0.0
    filtermatrix=[[1, 0, 0, 0, 0, 0, 0, 0, 1],[0, 1, 0, 0, 0, 0, 0, 1, 0],[0, 0, 1, 0, 0, 0, 1, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0, 0],[0, 0, 1, 0, 0, 0, 1, 0, 0],[0, 1, 0, 0, 0, 0, 0, 1, 0],[1, 0, 0, 0, 0, 0, 0, 0, 1]]
elif(userin == 7):
    factor=1.0/9.0
    bias=0.0
    filtermatrix=[[1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 1]]
elif(userin == 8):
    factor=1.0/9.0
    bias=0.0
    filtermatrix=[[0, 0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0]]
elif(userin == 9):
    factor=1.0/16.0
    bias=128.0
    filtermatrix=[[-1,-2,-1],[-2,12,-2],[-1,-2,-1]]
elif(userin == 10):
    factor=1.0
    bias=0.0
    filtermatrix=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
elif(userin == 11):
    factor=1.0
    bias=0.0
    filtermatrix[[0,0,0,0,0],[0,0,0,0,0],[-1,-1,2,0,0],[0,0,0,0,0],[0,0,0,0,0]]
elif(userin == 12):
    factor=1.0
    bias=0.0
    filtermatrix=[[0,0,-1,0,0],[0,0,-1,0,0],[0,0,4,0,0],[0,0,-1,0,0],[0,0,-1,0,0]]
elif(userin == 13):
    factor=1.0
    bias=0.0
    filtermatrix=[[-1,0,0,0,0],[0,-2,0,0,0],[0,0,6,0,0],[0,0,0,-2,0],[0,0,0,0,-1]]
elif(userin == 14):
    factor=1.0
    bias=0.0
    filtermatrix=[[-5,0,0],[0,0,0],[0,0,5]]
elif(userin == 15):
    factor=1.0
    bias=0.0
    filtermatrix=[[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
elif(userin == 16):
    factor=1.0
    bias=0.0
    filtermatrix=[[0,-1,0],[-1,5,-1],[0,-1,0]]
elif(userin == 17):
    factor=1.0
    bias=0.0
    filtermatrix=[[0,-2,0],[-2,-11,-2],[0,-2,0]]
elif(userin == 18):
    factor=1.0/8.0
    bias=0.0
    filtermatrix=[[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,1],[-1,2,2,2-1],[-1,-1,-1,-1,-1]]
elif(userin == 19):
    factor=1.0
    bias=0.0
    filtermatrix=[[1,1,1],[1,-7,1],[1,1,1]]
elif(userin == 20):
    factor=1.0
    bias=128.0
    filtermatrix=[[2,0,0],[0,-1,0],[0,0,-1]]
elif(userin == 21):
    factor=1.0
    bias=128.0
    filtermatrix=[[-1,-1,0],[-1,0,1],[0,1,1]]
elif(userin == 22):
    factor=1.0
    bias=128.0
    filtermatrix=[[-1,0,0],[0,0,0],[0,0,1]]
elif(userin == 23):
    factor=1.0
    bias=128.0
    filtermatrix=[[-1,-1,-1,-1,0],[-1,-1,-1,0,1],[-1,-1,0,1,1],[-1,0,1,1,1],[0,1,1,1,1]]
else:
    print "invalid input"


filterwidth=len(filtermatrix)
filterheight=len(filtermatrix[0])

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
        if(x>=offsetx and y>=offsety and x < width and y <height):
            cpixel=pixels[x-offsetx,y-offsety]
            j.putpixel((x,y),cpixel)


for y in range(height+(2*offsety)):
    for x in range(width+(2*offsetx)):
        if(x>=offsetx and y>=offsety and x < width and y <height):
            blue=0.0
            green=0.0
            red=0.0
            filterx=x-offsetx
            filtery=y-offsety
            for fy in range(filterheight):
                for fx in range(filterwidth):
                    cpixel=j.getpixel((x-offsety+fx,y-offsety+fy))
                    red+=float(cpixel[0])*filtermatrix[fx][fy]
                    green+=float(cpixel[1])*filtermatrix[fx][fy]
                    blue+=float(cpixel[2])*filtermatrix[fx][fy]
            red=(factor*red)+bias
            green=(factor*green)+bias
            blue=(factor*blue)+bias
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
            k.putpixel((x-offsetx,y-offsety),(int(red),int(green),int(blue)))
k.save('output.png')
