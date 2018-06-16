import random
import grid
import location as p
class Human:
    def __init__(self, piece):
        self.piece = piece
    def getMove(self, board):
        #first get all allowed moves then choose one at random
        x = int(input())
        y = int(input())
        return [x,y]
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def __str__(self):
        return self.piece
