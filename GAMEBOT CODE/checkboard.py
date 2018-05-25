#import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BCM)
outputs = [18, 23, 24, 25, 12, 16, 20, 21]
inputs = [4, 17, 27, 22, 5, 6, 13, 19]
boardState = [
    #a  b  c  d  e  f  g  h
    [1, 0, 1, 0, 1, 0, 1, 0], #8
    [0, 1, 0, 1, 0, 1, 0, 1], #7
    [1, 0, 1, 0, 1, 0, 1, 0], #6
    [0, 0, 0, 0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 0, 0, 0, 0], #4
    [0, 1, 0, 1, 0, 1, 0, 1], #3
    [1, 0, 1, 0, 1, 0, 1, 0], #2
    [0, 1, 0, 1, 0, 1, 0, 1]  #1
]


for outPin in range (0, 8):
    #GPIO.setup(outputs[outPin], GPIO.OUT)
    print (outputs[outPin])

for inPin in range (0,8):
    #GPIO.setup(inputs[inPin], GPIO.IN)
    print (inputs[inPin])


#print (boardState[4][7])

def WhereAreSquares(): #transmitters need to be horizontal & pickups need to be vertical when wired
    for send in range (0, 8):
        GPIO.output(outputs[send], 1)
        for receive in range (0, 8):
            if GPIO.input(inputs[receive]):
                #boardState[send][receive] = 1
                print (boardState[send][receive])
            else:
                #boardState[send][receive] = 0
                print (boardState[send][receive])
                
                
