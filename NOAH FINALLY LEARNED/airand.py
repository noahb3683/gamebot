import random
import grid
import location as p
class AIrand:
    def __init__(self, piece):
        self.piece = piece
    def getMove(self, board):
        #first get all allowed moves then choose one at random
        allowed_moves = []
        for i in range(board.getSize()):
            for j in range(board.getSize()):
                if board.get(p.location(i,j)) == " ":
                    allowed_moves.append([i,j])
        return random.choice(allowed_moves)
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def __str__(self):
        return self.piece
