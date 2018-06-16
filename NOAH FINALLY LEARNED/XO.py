import turnManager
import location as p
import grid
class XO:
    def __init__(self, board_size, players):
        self.turnM = turnManager.turnManager(players)
        self.board = grid.grid(' ', board_size)
        self.recent_move = p.location(-1,-1)
        self.board_size = board_size
    def updateBoard(self, inBoard):
        for i in range(self.board.getSize()):
            for j in range(self.board.getSize()):
                if inBoard[i][j] == 1 and self.board.get(p.location(i, j)) == " ":
                    self.board.set(p.location(i,j), self.turnM.currentPlayer())
                    #Success
                    self.recent_move.update(i, j)
                    return 1
        #No update
        print("nothing changed")
        return 0
    def checkForWin(self):
        #Rows
        for i in range(self.board_size):
            if not self.board.get(p.location(self.recent_move.row(), i)) == self.turnM.currentPlayer():
                break
            if i == (self.board_size-1):
                return str(self.turnM.currentPlayer()) + " wins"
        #Column
        for i in range(self.board_size):
            if not self.board.get(p.location(i, self.recent_move.column())) == self.turnM.currentPlayer():
                break
            if i == (self.board_size-1):
                return str(self.turnM.currentPlayer()) + " wins"
        #Diag
        if self.recent_move.row() == self.recent_move.column():
            for i in range(self.board_size):
                if not self.board.get(p.location(i, i)) == self.turnM.currentPlayer():
                    break
                if i == (self.board_size-1):
                    return str(self.turnM.currentPlayer()) + " wins"
        #Other Diag
        if (self.recent_move.row() + self.recent_move.column()) == (self.board_size - 1):
            for i in range(self.board_size):
                if not self.board.get(p.location(i, (self.board_size-1)-i)) == self.turnM.currentPlayer():
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

