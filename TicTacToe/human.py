import random
import grid
import location as p
'''
Allows human to play by taking in their move from console input
'''
class Human:
    def __init__(self, piece, oppopiece):
        self.piece = piece
        print("A human is", piece)
        print("Human enters moves:")
        print("(row #)\n(column #)\n")
        self.oppopiece = oppopiece
    def getMove(self, board):
        x = int(input())
        y = int(input())
        return [x,y]
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def __str__(self):
        return self.piece
