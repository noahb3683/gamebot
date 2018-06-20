import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
outputs = [12, 16, 18] # 22, 32, 36, 38, 40]
inputs = [31, 33, 35] # 15, 29,31, 33, 35]
'''boardState = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
]'''
boardState = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for outPin in range(0, 3):
    GPIO.setup(outputs[outPin], GPIO.OUT)
    print (outputs[outPin], "poi")

for inPin in range(0, 3):
    GPIO.setup(inputs[inPin], GPIO.IN)
    print (inputs[inPin], "koi")

def WhereAreSquares():
    GPIO.output(12, 1)
    if GPIO.input(31):
        print ("31, 12")
        boardState[2][0] = 1
    if GPIO.input(33):
        print ("33, 12")
        boardState[2][1] = 1
    if GPIO.input(35):
        print ("35, 12")
        boardState[2][2] = 1
    GPIO.output(12, 0)
    GPIO.output(16, 1)
    if GPIO.input(31):
        print ("31, 16")
        boardState[1][0] = 1
    if GPIO.input(33):
        print ("33, 16")
        boardState[1][1] = 1
    if GPIO.input(35):
        print ("35, 16")
        boardState[1][2] = 1
    GPIO.output(16, 0)
    GPIO.output(18, 1)
    if GPIO.input(31):
        print ("31, 18")
        boardState[0][0] = 1
    if GPIO.input(33):
        print ("33, 18")
        boardState[0][1] = 1
    if GPIO.input(35):
        print ("35, 18")
        boardState[0][2] = 1
    GPIO.output(18, 0)

        
WhereAreSquares()
for poicon in boardState:
    print (poicon)
GPIO.cleanup()

