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
    def __init__(self, piece):
        self.piece = piece

    def generateHops(self, position, piece):
        p = self.piece if len(piece)==1 else " "
        output = list()
        for f in self.forward[p]:
            temp = position+self.directions[f]
            if temp.valid():
                output.append(temp)
        return output
    def checkForHops(self, board):
        for i in range(8):
            for j in range(8):
                l = p.location(i, j)
                e = board.get(l)
                if e == self.piece:
                    print(self.generateHops(l, e))
                    
                
    def getMove(self, board):
        self.checkForHops(board)       
        
        startLocation = p.location(np.random.randint(7, size=2))
        return startLocation
