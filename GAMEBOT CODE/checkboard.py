import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
outputs = [12, 16, 18, 22, 32, 36, 38, 40]
inputs = [7, 11, 13, 15, 29,31, 33, 35]
boardState = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
]


for outPin in range(0, 8):
    GPIO.setup(outputs[outPin], GPIO.OUT)
    print (outputs[outPin], "poi")

for inPin in range(0, 8):
    GPIO.setup(inputs[inPin], GPIO.IN)
    print (inputs[inPin], "koi")

def WhereAreSquares():
    for send in range(0, 8):
        GPIO.output(outputs[send], 1)
        for receive in range(0, 8):
            if GPIO.input(inputs[receive]):
                boardState[send][receive] = 1
                print ("LASERBOI HAS NAILED HIS TARGET")
            else:
                boardState[send][receive] = 0
                print ("nobody home & laserboi is a sad sad laserboi... :(")
WhereAreSquares()
for poicon in boardState:
    print (poicon)
GPIO.cleanup()
