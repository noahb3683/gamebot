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
    GPIO.output(31, 1)
    if GPIO.input(12)
        print ("31, 12")
    if GPIO.input(16)
        print ("31, 16")
    if GPIO.input(18)
        print ("31, 18")
    GPIO.output(31, 0)
    GPIO.output(33, 1)
    if GPIO.input(12)
        print ("33, 12")
    if GPIO.input(16)
        print ("33, 16")
    if GPIO.input(12)
        print ("33, 18")
    GPIO.output(33, 0)
    GPIO.output(35, 1)
    if GPIO.input(12)
        print ("35, 12")
    if GPIO.input(12)
        print ("35, 16")
    if GPIO.input(12)
        print ("35, 18")
    GPIO.output(35, 0)

        
WhereAreSquares()
for poicon in boardState:
    print (poicon)
GPIO.cleanup()

