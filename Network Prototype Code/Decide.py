import socket
import pickle
import pyttsx3 as tts #Text-to-speach Library
from time import sleep

TCP_IP_DECT = '127.0.0.1'
TCP_PORT_DECT = 1241
TCP_IP_MOVE = '127.0.0.1'
TCP_PORT_MOVE = 5006
BUFFER_SIZE = 1024

def findMove(board):
    print("Board is:")
    for row in board:
        print(row)
    move = {"x1":0, "y1":1, "x2":2, "y2":3}
    return move

def main():
    #Listenning socket to receive from Detection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP_DECT, TCP_PORT_DECT))
    s.listen(1)

    stay = True
    while stay:
        conn, addr = s.accept()
        print ('Connected to: ', addr)
        data = conn.recv(BUFFER_SIZE)
        board = pickle.loads(data)
        if not data: stay = False
        sleep(3)
        #Socket made to send to Move
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect((TCP_IP_MOVE, TCP_PORT_MOVE))
        #Put function to generate move here
        move = findMove(board)
        #send move to MovePI
        s2.send(pickle.dumps(move))
        s2.close()
        #Put code to send what board should be here
        conn.send("YOUR TURN".encode())
        conn.close()
main()
