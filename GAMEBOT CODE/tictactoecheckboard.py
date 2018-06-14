import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
outputs = [12, 16, 18] #22, 32, 36, 38, 40]
inputs = [7, 11, 13] #15, 29, 31, 33, 35]
'''boardState = [
    #a  b  c  d  e  f  g  h
    [1, 0, 1, 0, 1, 0, 1, 0], #8
    [0, 1, 0, 1, 0, 1, 0, 1], #7
    [1, 0, 1, 0, 1, 0, 1, 0], #6
    [0, 0, 0, 0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 0, 0, 0, 0], #4
    [0, 1, 0, 1, 0, 1, 0, 1], #3
    [1, 0, 1, 0, 1, 0, 1, 0], #2
    [0, 1, 0, 1, 0, 1, 0, 1]  #1
]'''
#legacy checkers array

boardState = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for outPin in range (0, 3): # 3 by 3 grid
    GPIO.setup(outputs[outPin], GPIO.OUT)
    print (outputs[outPin], "Poi")

for inPin in range (0,3): # 3 by 3 grid
    GPIO.setup(inputs[inPin], GPIO.IN)
    print (inputs[inPin], "Koi")


#print (boardState[yuudachi][poi]) test

def WhereAreSquares(): #transmitters need to be horizontal & pickups need to be vertical when wired
    for send in range (0, 3): # 3 by 3 grid
        GPIO.output([outputs], 1)
        for receive in range (0, 3): # 3 by 3 grid
            if GPIO.input([inputs]):
                boardState[send][receive] = 1
                print (boardState[send][receive])
            else:
                boardState[send][receive] = 0
                print (boardState[send][receive])
                
                
