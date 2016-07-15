from Myro import *

def obamafication():
    picture = pickAFile()
    pic = makePicture(picture)
    pixels = getPixels(pic)
    oDB = makeColor(0,51,76)
    oR = makeColor(217, 26, 33)
    oB = makeColor(112,150,158)
    oY = makeColor(252, 227, 166)
    
    for pxl in pixels:
        gray = getGray(pxl)
        if gray > 180:
            setColor(pxl, oY)
        elif gray > 120:
            setColor(pxl, oB)
        elif gray < 60:
            setColor(pxl, oR)
        else:
            setColor(pxl, oDB)
            
    show(pic)
obamafication()