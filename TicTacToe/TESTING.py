import socket
import pickle

TCP_IP = '127.0.0.1'
TCP_PORT = 1241
BUFFER_SIZE = 1024

while True:
    print("Your move")
    x = int(input())
    y = int(input())
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((TCP_IP, TCP_PORT))
    s2.send(pickle.dumps([x,y]))
    s2.close()
