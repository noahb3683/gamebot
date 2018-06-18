import socket
import pickle
from time import sleep
import pyttsx3 as tts

engine = tts.init()

def say(words):
    engine.say(words)
    engine.runAndWait()

TCP_IP = '127.0.0.1'
TCP_PORT = 1241
BUFFER_SIZE = 1024
MESSAGE = "HELLO!"

lastBoard = [
["x", " ", "x"," ", " ", "x"," ", " "],
[" ", "x", "x"," ", " ", "x"," ", " "],
[" ", " ", "x"," ", " ", "x"," ", " "],
[" ", " ", "x","x", " ", "x"," ", " "],
[" ", " ", "x"," ", "x", "x"," ", " "],
[" ", " ", "x"," ", " ", "x","x", " "],
[" ", " ", "x"," ", " ", "x"," ", "x"],
[" ", " ", "x"," ", " ", "x"," ", "o"]]
def poll():
    #Gets current board from sensors
    currentBoard = [
    ["x", " ", "x"," ", " ", "x"," ", " "],
    [" ", "x", "x"," ", " ", "x"," ", " "],
    [" ", " ", "x"," ", " ", "x"," ", " "],
    [" ", " ", "x","x", " ", "x"," ", " "],
    [" ", " ", "x"," ", "x", "x"," ", " "],
    [" ", " ", "x"," ", " ", "x","x", " "],
    [" ", " ", "x"," ", " ", "x"," ", "x"],
    [" ", " ", "x"," ", " ", "x"," ", "o"]]
    return currentBoard

def waitForHuman():
    while 1:
        currentBoard = poll()
        if currentBoard != lastBoard:
            return currentBoard
        sleep(0.5)

def main():
    while 1:
        sleep(1.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        #Put code to detect board here
        s.send(pickle.dumps(lastBoard))
        data = s.recv(BUFFER_SIZE).decode()
        s.close()
        print("received: ", data)
        say(data)
main()
