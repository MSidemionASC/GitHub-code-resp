from Processing import *
from random import *
#Shinjini Nunna
#July 20 2016
#Bouncing Ball Lab - ball bounces randomly within walls displayed onscreen


window(600,600) #set up display

#set up playing field
fill(255,255,255)
rect(20,20,400,400)
#variables storing x and y coordinate of ball
ballX = 220
ballY = 220
#creates image of ball in display
fill(255,0,0)
ellipseMode(CORNER)
ellipse(ballX,ballY,30,30)

#randomly choose amount by which to change the x and y coordinates
#of the ball
xChange = randrange(-3,3)
yChange = randrange(-3,3)

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
    fill(255,0,0)
    ellipse(ballX, ballY, 30,30)
    delay(5) #wait so that human eye can process move
    
    if (ballX >= 389): #bounce off right wall
        xChange = -1
        yChange = randrange(-3,3)
    
    if (ballX <= 21): #bounce off left wall
        xChange = 1
        yChange = randrange(-3,3)
    if (ballY >= 389): #bounce off bottom wall
        xChange = randrange(-3,3)
        yChange = -1
    
    if (ballY <= 21): #bounce off top wall
        xChange = randrange(-3,3)
        yChange = 1        
      
