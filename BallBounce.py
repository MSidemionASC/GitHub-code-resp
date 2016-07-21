from Processing import *
from random import * 
window(500,500)

#wall1 = line(10,10,490,10)
#wall2 = line(10,10,10,490)
#wall3 = line(10,490,490,490)
#wall4 = line(490,490,490,10)

red = randrange(0,255)
green = randrange(0, 255)
blue = randrange(0, 255)



background(255,255,255)
#variables storing x and y coordinate of ball
ballX = 250
ballY = 250
#creates image of ball in display
fill(255,0,0)
ellipseMode(CORNER)
ellipse(ballX,ballY,70,70)

#randomly choose amount by which to change the x and y coordinates
#of the ball
xChange = randrange(-5,5)
yChange = randrange(-5,5)

while True:
    #change the x and y coordinates of the ball
    #to make it look like ball is "moving"
    ballX = ballX + xChange
    ballY = ballY + yChange
    
    #new background to cover up previous image of ball
    background(255,255,255)
    #set up walls again since previous walls are now covered
    #by the new background from line above
    fill(255,255,255)
    rect(20,20,400,400)
    #create new image of the ball at new x and y coordinates
    fill(red, green, blue)
    ellipse(ballX, ballY, 30,30)
    delay(3) #wait so that human eye can process move
    
    if (ballX >= 470): #bounce off right wall
        fill(red, green, blue)
        ellipse(ballX, ballY, 30,30)
        xChange = -1
        yChange = randrange(-5,5)
    
    if (ballX <= 20): #bounce off left wall
        fill(red, green, blue)
        ellipse(ballX, ballY, 30,30)
        xChange = 1
        yChange = randrange(-5,5)
    if (ballY >= 470): #bounce off bottom wall
        fill(red, green, blue)
        ellipse(ballX, ballY, 30,30)
        xChange = randrange(-5,5)
        yChange = -1
    
    if (ballY <= 10): #bounce off top wall
        fill(red, green, blue)
        ellipse(ballX, ballY, 30,30)
        xChange = randrange(-5,5)
        yChange = 1  

