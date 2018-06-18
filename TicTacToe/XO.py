import turnManager
import location as p
import grid
"""
Class to play XO on board of size given
Could be used to play multi piece checkers
"""
class XO:
    def __init__(self, board_size, players):
        self.turnM = turnManager.turnManager(players)
        self.board = grid.grid(' ', board_size)
        self.recent_move = p.location(-1,-1)
        self.board_size = board_size
    def updateBoard(self, inBoard):
        """
        Takes 2d  array of 1/0 's and converts to string board
        """
        for i in range(self.board.getSize()):
            for j in range(self.board.getSize()):
                if inBoard[i][j] == 1 and self.board.get(p.location(i, j)) == " ":
                    self.board.set(p.location(i,j), self.turnM.currentPlayer().getPiece())
                    #Success
                    self.recent_move.update(i, j) #Store the most recent move to make checking for win faster
                    return 1
        #No update
        print("nothing changed")
        return 0
    def checkForWin(self):
        """
        If game over returns player piece and 'wins' to be printed
        Elif game stalemate returns stalemate
        Else returns nothing
        """
        #Rows
        for i in range(self.board_size):
            if not self.board.get(p.location(self.recent_move.row(), i)) == self.turnM.currentPlayer().getPiece():
                break
            if i == (self.board_size-1):
                return str(self.turnM.currentPlayer()) + " wins"
        #Column
        for i in range(self.board_size):
            if not self.board.get(p.location(i, self.recent_move.column())) == self.turnM.currentPlayer().getPiece():
                break
            if i == (self.board_size-1):
                return str(self.turnM.currentPlayer()) + " wins"
        #Diag
        if self.recent_move.row() == self.recent_move.column():
            for i in range(self.board_size):
                if not self.board.get(p.location(i, i)) == self.turnM.currentPlayer().getPiece():
                    break
                if i == (self.board_size-1):
                    return str(self.turnM.currentPlayer()) + " wins"
        #Other Diag
        if (self.recent_move.row() + self.recent_move.column()) == (self.board_size - 1):
            for i in range(self.board_size):
                if not self.board.get(p.location(i, (self.board_size-1)-i)) == self.turnM.currentPlayer().getPiece():
                    break
                if i == (self.board_size-1):
                    return str(self.turnM.currentPlayer()) + " wins"
        #Stalemate
        if self.turnM.count() == self.board_size**2:
            return "Stalemate"
        return None
    def printBoard(self):
        print(self.board)
    def start(self):
        self.turnM.randomizePlayer()
    def currentPlayer(self):
        return self.turnM.currentPlayer()
    def nextTurn(self):
        self.turnM.nextTurn()

