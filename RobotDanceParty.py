from Myro import *

def danceMoveOne():
    backward(1, .5)
    forward(1, .5)
    backward(1, .5)
    forward(1, .5)
def danceMoveTwo():
    motors(-1, 1, .4)
    backward(1, .5)
    forward(1, .5)
    backward(1, .5)
    forward(1, .5)
    backward(1, 1)
def danceMoveThree():
    motors(1, -1, .8)
    forward(1, 1)
    backward(1, .5)
    forward(1, .5)
    backward(1, .5)
    forward(1, .5)
def danceMoveFour():
    backward(1, 1)
    motors(-1, 1, .4)
    backward(1, .5)
    forward(1, .5)
    motors(-1, 1, 7)
    motors(1, -1, 7)
def danceMoveFive():
    backward(1, .5)
    forward(1, .5)
    motors(-1, 1, 7)
    motors(1, -1, 7)
def danceMoveSix():
    backward(1, .3)
def danceMoveSeven():
    forward(1, 3)
danceMoveSix()
danceMoveSeven()
danceMoveOne()
danceMoveOne()
danceMoveOne()
danceMoveTwo()
danceMoveThree()
danceMoveFour()
danceMoveFive()
danceMoveFive()


   
\ No newl
