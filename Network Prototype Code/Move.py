import socket
import pickle
from time import sleep

TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024



def move(start, end):
    print("start x: ", start["x"])
    print("start y: ", start["y"])
    print("end: ", end)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    while 1:
        conn, addr = s.accept()
        print ('Connected to: ', addr)
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            coor = pickle.loads(data)
            move({"x": coor['x1'],"y": coor['y1']},{"x": coor['x2'],"y": coor['y2']})
            sleep(2)
            conn.send("GO".encode())
        conn.close()
main()
