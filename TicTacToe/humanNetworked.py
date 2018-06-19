import random
import grid
import location as p

import socket
import pickle
'''
Allows human to play by taking in their move from TCP
'''
import pyttsx3 as tts

engine = tts.init()

TCP_IP_DECT = '127.0.0.1'
TCP_PORT_DECT = 1241
BUFFER_SIZE = 1024

def say(words):
    engine.say(words)
    engine.runAndWait()

class NetHuman:
    def __init__(self, piece, oppopiece):
        self.piece = piece
        print("A human is", piece)
        print("Human enters moves:")
        print("(row #)\n(column #)\n")
        self.oppopiece = oppopiece
    def getMove(self, board):
        say("Your Move")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP_DECT, TCP_PORT_DECT))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(BUFFER_SIZE)
        move = pickle.loads(data)
        conn.close()
        return move
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def __str__(self):
        return self.piece
