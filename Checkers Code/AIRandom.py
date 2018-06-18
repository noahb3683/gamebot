import location as p
import numpy as np
import grid

class AIRandom:
    directions = [
        [2,2],
        [2,-2],
        [-2,2],
        [-2,-2]
        ]
    forward = {"w":[0,1], "b":[2,3], " ":[0,1,2,3]} # selects which direction a piece can move
    pieceDict = {"w":"b", "b":"w"}
    def __init__(self, piece):
        self.piece = piece
        self.Oppopiece = self.pieceDict[piece]
    def generateHops(self, position, piece):
        p = self.piece if len(piece)==1 else " "
        output = list()
        for f in self.forward[p]:
            temp = position+self.directions[f]
            if temp.valid():
                output.append(temp)
        return output
    def findHops(self, piece, position, board):
        hops = list()
        for hop in self.generateHops(position, piece):
            direction = hop-position
            for i in range(2):
                direction[i] = round(direction[i]/2)
            direction = direction+position
            if board.get(hop) == " " and board.get(direction) == self.Oppopiece:
                return [position, hop] #this is a hop that has to be taken for this AI always take first hop found
        return None
    def checkForHops(self, board):
        for i in range(8):
            for j in range(8):
                pos = p.location(i, j)
                e = board.get(pos)
                if e[0] == self.piece:
                    temp = self.findHops(e, p.location(i, j), board)
                    if temp: return temp
        return None
    def getMove(self, board):
        output = list()
        temp = self.checkForHops(board)
        if temp:
            done = False
            output = temp
            while not done:
                t = self.findHops(self.piece, output[len(output)-1], board)
                if t:
                    output.append(t[1])
                else:
                    done = True
            return output
        
        startLocation = p.location(np.random.randint(7, size=2))
        return None
    def test(self):
        print(self.generateHops(p.location(7,6), "wk"))
