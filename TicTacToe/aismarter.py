import random
import grid
import location as p
import numpy as np
'''
Looks all the moves ahead to check if it or its opponent can win
https://medium.freecodecamp.org/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37
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
        self.preCalc = {} #Dictionary of boardstates and players with best move
    def allowedMoves(self, board):
        allowed_moves = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    allowed_moves.append([i,j])
        return allowed_moves
    def minMax(self, board, player):
        """
        Uses dictionary of (board and player) to save recursion
        """
        b = np.array(board) #use numpy to flatten and merge
        b = b.reshape((len(board)**2)) #Flatten
        b = np.concatenate((b, np.array([player]))) #add player to end
        b = tuple(b) #Convert to tuple since need imutable object
        if b in self.preCalc:
            return self.preCalc[b]
        allowed = self.allowedMoves(board)
        temp = self.checkForWin(board)
        if temp == self.piece:
            return [1+random.random()]#To prevent first move from always taken
        elif temp == self.oppopiece:
            return [-1-random.random()]#adds some unpredicatability to AI
        elif len(allowed) == 0:
            return [0]
        moves = []
        for move in allowed:
            temp = []
            tempBoard = board
            tempBoard[move[0]][move[1]] = player
            if player == self.piece:
                score = self.minMax(tempBoard, self.oppopiece)
                temp.append(score[0])#Keep just the score
            else:
                score = self.minMax(tempBoard, self.piece)
                temp.append(score[0])
            temp.append(move)#store location
            tempBoard[move[0]][move[1]] = " "#Make sure to reset board
            moves.append(temp)
        """
        Find highest scoring/lowest scoring move
        Find highest on its turn
        Finds lowest on oppo's turn
        """
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
        self.preCalc[b] = (best,spot)
        return [best,spot]
    def getMove(self, board):
        return self.minMax(board.getGrid(), self.piece)[1] #return move only
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
