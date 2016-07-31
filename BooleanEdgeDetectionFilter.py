# Author Bhargav K
# Email bhargav.gamit@gmail.com
# Morphological Filters
# BooleanEdgeDetectionFilter

import sys
from PIL import Image
i = Image.open("input.png")

#store pixels of input image
pixels = i.load()
width, height = i.size
k=Image.new(i.mode,i.size)

print "Choose BooleanFilterType"
print "1 None"
print "2 EdgeDetect"
print "3 Sharpen"
filtertype=input()
filtersize=input("Choose the Size of Filter (Usually 3) : ")
print "Usually 1.0"
redfactor=input("Enter red factor value   : ")
greenfactor=input("Enter green factor value : ")
bluefactor=input("Enter blue factor value  : ")
threshold=input("Enter Threshold value (0.0 to 200.0):")

edgemasks=[]
edgemasks.append("011011011")
edgemasks.append("000111111")
edgemasks.append("110110110")
edgemasks.append("111111000")
edgemasks.append("011011001")
edgemasks.append("100110110")
edgemasks.append("111011000")
edgemasks.append("111110000")
edgemasks.append("111011001")
edgemasks.append("100110111")
edgemasks.append("001011111")
edgemasks.append("111110100")
edgemasks.append("000011111")
edgemasks.append("000110111")
edgemasks.append("001011011")
edgemasks.append("001011011")
edgemasks.append("110110100")

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
        if(x>=offsetx+1 and y>=offsety+1 and x <=width and y <=height):
            matrixmean=0
            matrixtotal=0
            matrixvariance=0.0
            matrixpattern=''
            filterx=x-offsetx
            filtery=y-offsety
            for fy in range(filterheight):
                for fx in range(filterwidth):
                    cpixel=j.getpixel((x-offsety+fx,y-offsety+fy))
                    matrixmean+=(cpixel[0])
                    matrixmean+=(cpixel[1])
                    matrixmean+=(cpixel[2])
            matrixmean=matrixmean/9
            for fy in range(filterheight):
                for fx in range(filterwidth):
                    cpixel=j.getpixel((x-offsety+fx,y-offsety+fy))
                    matrixtotal=(cpixel[0])
                    matrixtotal+=(cpixel[1])
                    matrixtotal+=(cpixel[2])
                    if(matrixtotal>matrixmean):
                        matrixpattern+='1'
                    else:
                        matrixpattern+='0'
                    matrixvariance+=pow(matrixmean-(cpixel[0]+cpixel[1]+cpixel[2]),2)
            matrixvariance=matrixvariance/9.0
            cpixel=j.getpixel((x,y))
            if(filtertype==3):
                red=cpixel[0]
                green=cpixel[1]
                blue=cpixel[2]
                if(matrixvariance>threshold):
                    if(matrixpattern in edgemasks):
                        red=int(red*redfactor)
                        green=int(green*greenfactor)
                        blue=int(blue*bluefactor)
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
            elif(matrixvariance>threshold and (matrixpattern in edgemasks)):
                red=255
                green=255
                blue=255
            else:
                red=0
                green=0
                blue=0
            del matrixpattern
            k.putpixel((x-offsetx,y-offsety),(int(red),int(green),int(blue)))
k.save('output.png')
