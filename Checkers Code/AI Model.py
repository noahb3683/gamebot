import location as p
import numpy as np
import grid

class AIRandom:
    def __init__(self, piece):
        self.piece = piece
    def getMove(self, board):
        startLocation = p.location(np.random.randint(7, size=2))
        return startLocation
