from Processing import *
size(900,900)
white = color(255,255,255)
red = color(255,0,0)
green = color(0,255,0)
blue = color(0,0,255)
yellow = color(255,255,0)
orange = color(255,165,0)
black = color(0,0,0)
colors = [white,red,green,blue,yellow,orange,black]


def draw():
       global colors
       i = 0
       x = 0
       while (i<len(colors)):
        fill(colors[i])
        rect(x,0,width()/len(colors),width()/len(colors))
        x += width()/len(colors)
        i+=1
       

 

def doMouseDragged():
    #userThick = int(input("how thick do you want your strokes to be?"))*10
    #strokeWeight(userThick)
    gate = width()/len(colors)
    if(mouseY()>gate+20):
        line(pmouseX(), pmouseY(), mouseX(), mouseY())
  
def MouseClickedColor():
    gate = width()/len(colors)
    if(mouseY()<gate):
        i = 0
        while(gate<=width()):
            if(mouseX()<=gate):
                stroke(colors[i])
                break;
            else:
                gate+= width()/len(colors)
            i+=1

    
onMouseClicked += MouseClickedColor
onMouseDragged += doMouseDragged
draw()
