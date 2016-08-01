from Processing import *
from random import *

#size of the playing field
window(600,600)

#background color
background(0,0,0)

#the color of the user ship



#the color of the enemy ship


shipX = 300

        
def draw():
    while True:
        global shipX
        noStroke()
        rectMode(CENTER)
        fill(124,252,0)
        rect(shipX, 500, 60, 20)
        rect(shipX, 490, 10, 20)
        if isKeyPressed() == True:
            if key()=="a":
                shipX-=5
            if key()=="d":
                shipX+=5
draw()    
