#import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BCM)
outputs = [18, 23, 24, 25, 12, 16, 20, 21]
inputs = [4, 17, 27, 22, 5, 6, 13, 19]
boardState = [
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1]
]


for outPin in range (0, 8):
    #GPIO.setup(outputs[outPin], GPIO.OUT)
    print (outputs[outPin])

for inPin in range (0,8):
    #GPIO.setup(inputs[inPin], GPIO.IN)
    print (inputs[inPin])


print (boardState[4][7])

def WhereAreSquares():
    for send in range (0, 8):
        GPIO.output([outputs], 1)
        for receive in range (0, 8):
            if GPIO.input([inputs]):
                #boardState[send][receive] = 1
                print (boardState[send][receive])
            else:
                #boardState[send][receive] = 0
                print (boardState[send][receive])
                
                
