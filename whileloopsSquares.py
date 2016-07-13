from Myro import *
init("sim")

def square():
    i = 0
    while(i < 4):
        penDown("red")
        forward(1, 2)
        turnBy(90, "deg")
        i = i + 1
        penUp()
    forward(1, 4)
square()
square()
    
