import random
import grid
import location as p
import numpy as np
'''
Looks two moves ahead to check if it or its opponent can win
Else picks random allowed move
'''
class AIsmarter:
    def __init__(self, piece, oppopiece):
        self.piece = piece
        self.oppopiece = oppopiece
        self.corners = [
            [0,0],
            [2,0],
            [0,2],
            [2,2]
            ]
    def allowedMoves(self, board):
        allowed_moves = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    allowed_moves.append([i,j])
        return allowed_moves
    def minMax(self, board, player):
        #print(board)
        allowed = self.allowedMoves(board)
        temp = self.checkForWin(board)
        if temp == self.piece:
            return [1]
        elif temp == self.oppopiece:
            return [-1]
        elif len(allowed) == 0:
            return [0]
        moves = []
        for move in allowed:
            temp = []
            tempBoard = board
            tempBoard[move[0]][move[1]] = player
            if player == self.piece:
                score = self.minMax(tempBoard, self.oppopiece)
                temp.append(score[0])
            else:
                score = self.minMax(tempBoard, self.piece)
                temp.append(score[0])
            temp.append(move)#store location
            tempBoard[move[0]][move[1]] = " "
            moves.append(temp)
        #Find best move
        if player == self.piece:
            best = -10000
            for move in moves:
                if move[0] > best:
                    best = move[0]
                    spot = move[1]
        else:
            best = 10000
            for move in moves:
                if move[0] < best:
                    best = move[0]
                    spot = move[1]
        return [best,spot]
    def getMove(self, board):
        #first get all allowed moves then choose one at random
        b = np.array(board.getGrid())
        b = b.reshape((len(board.getGrid())**2))
        if not "x" in b and not "o" in b:
            return [0,0]
        return self.minMax(board.getGrid(), self.piece)[1]
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
