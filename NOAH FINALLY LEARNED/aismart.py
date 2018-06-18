import random
import grid
import location as p
import numpy as np
'''
Looks one move ahead to check if it or its opponent can win
Else picks random allowed move
'''
class AIsmart:
    def __init__(self, piece, oppopiece):
        self.piece = piece
        self.oppopiece = oppopiece
        self.corners = [
            [0,0],
            [2,0],
            [0,2],
            [2,2]
            ]
    def getMove(self, board):
        #first get all allowed moves then choose one at random
        allowed_moves = []
        for i in range(board.getSize()):
            for j in range(board.getSize()):
                if board.get(p.location(i,j)) == " ":
                    allowed_moves.append([i,j])
        output = []
        for move in allowed_moves:#check to see if someone can win next turn
            tempBoard = board.getGrid()
            tempBoard[move[0]][move[1]] = self.piece
            if self.checkForWin(tempBoard) == self.piece:
                output = move
                tempBoard[move[0]][move[1]] = " "
                break
            tempBoard[move[0]][move[1]] = self.oppopiece
            if self.checkForWin(tempBoard) == self.oppopiece:
                output = move
                tempBoard[move[0]][move[1]] = " "
                break
            tempBoard[move[0]][move[1]] = " "
        else:
            output = random.choice(allowed_moves)
        return output
    def checkForWin(self, board):
        b = np.array(board)
        size = len(board)
        for i in range(size):
            if all(b[i][j] == b[i][j-1] for j in range(1, size)) and not b[i][0] == " ":
                return b[i][0] #horizontal win
        for i in range(size):
            if all(b[:,i][j] == b[:,i][j-1] for j in range(1, size)) and not b[:,i][0] == " ":
                return b[:,i][0] #vertical win
        for i in range(1,size):
            if not b[i-1][i-1] == b[i][i] or b[i][i] == " ":
                break
        else:
            return b[0][0] # diagonal win
        for i in range(size-1):
            if not b[i][(size-1)-i] == b[i+1][(size-1)-(i+1)] or b[i][(size-1)-i] == " ":
                break
        else:
            return b[0][size-1] # diagonal win
        return None
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def __str__(self):
        return self.piece
