from Processing import *
from random import *
window(500,500)
# setting the size of the playing 

sea = [[0,1,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
#for i in range(len(

i = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0 
x = 0
x2 = 0
x3 = 0
x4 = 0
x5 =0
y = 0
while i < 5:
    fill(255,255,255)
    rect(x,y,100,100)
    x = x + 100
    i = i + 1
while i2 < 5:
    fill(255,255,255)
    rect(x2,100,100,100)
    x2 = x2 + 100
    i2 = i2 + 1  
while i3 < 5:
    fill(255,255,255)
    rect(x3,200,100,100)
    x3 = x3 + 100
    i3 = i3 + 1 
while i4 < 5:
    fill(255,255,255)
    rect(x4,300,100,100)
    x4 = x4 + 100
    i4 = i4 + 1 
while i5 < 5:
    fill(255,255,255)
    rect(x5,400,100,100)
    x5 = x5 + 100
    i5 = i5 + 1
    
userX= int(input("enter 1st cord number between 0 and 4"))
userY = int(input("enter 2nd cord number between 0 and 4"))
if sea[userX][userY]== sea[shipX][shipY]:
        fill(0,255,0)
        rect(userX*100,userY*100,100,100)
        print("You hit it")
shipX = 0
shipY = 1
missed = 0
triesLeft = 5
while userX != shipX and userY != shipY and missed < 5 :
    userX= int(input("enter 1st cord number between 0 and 4"))
    userY = int(input("enter 2nd cord number between 0 and 4"))  
    sea[userX][userY]
    if sea[userX][userY] == sea[shipX][shipY]:
        fill(0,255,0)
        rect(userX*100,userY*100,100,100)
        print("You hit it")
    else:
        print("That was a miss")
        fill(255,0,0)
        rect(userX*100,userY*100,100,100)
        missed = missed + 1
        triesLeft = 5
        triesLeft = triesLeft-missed
        print("You have " + triesLeft + " tries left")
    if triesLeft == 0:
        print("You have no more tries. GAME OVER")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 