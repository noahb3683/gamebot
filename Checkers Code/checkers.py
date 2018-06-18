import location as p
import grid
import turnManager as t
boardSize = 8
"""
Assumes there is a physical board that is sending true/false table of piece locations
This just stores the board as a 2d array of strings from the true/false table
Needs to be called from master loop:

getBoard() returns board object, can be directly printed
updateBoard() takes true/false table passed and updates string version
check() returns if a player has won, returning that player piece
nextTurn() changes active player
"""
class checkers:
    def possibleMoves(self, startLocation, piece):
        #used to find possible moves in order to find valid moves
        #Don't directly call
        if piece == "w":
            Moves = list()
            Moves.append(p.location(startLocation.row()+1, startLocation.column()-1))
            Moves.append(p.location(startLocation.row()+1, startLocation.column()+1)) 
        elif piece == "b":
            Moves = list()
            Moves.append(p.location(startLocation.row()-1, startLocation.column()-1))
            Moves.append(p.location(startLocation.row()-1, startLocation.column()+1))
        else:
            Moves = list()
            Moves.append(p.location(startLocation.row()-1, startLocation.column()-1))
            Moves.append(p.location(startLocation.row()-1, startLocation.column()+1))
            Moves.append(p.location(startLocation.row()+1, startLocation.column()-1))
            Moves.append(p.location(startLocation.row()+1, startLocation.column()+1)) 
        return Moves
    def validMoves(self, startLocation, piece):
        #This finds all moves on the board from given location for a piece
        #Doesn't check if squares are open
        moves = self.possibleMoves(startLocation, piece)
        i = 0
        while i < len(moves):
            m = moves[i]
            if not m.valid():
                moves.remove(m)
            else:
                i+=1
        return moves
    def CheckMoves(self, board, moves, startLocation):
        #checks to see if moves land on open squares
        for m in moves:
            if board.get(m) == " ":
                return True
            m.update(2*m.row()-startLocation.row(), 2*m.column()-startLocation.row())
            if board.get(m) == " ":
                return True
        return False
    def CheckForStalemate(self, board):
        #Checks to see if a player can't move
        canMove = {"b":False, "w":False}
        for r in range(8):
            for c in range(8):
                thisLocation = p.location(r, c)
                piece = board.get(thisLocation)
                if piece == " ": continue
                moves = self.validMoves(thisLocation, piece)
                hasMove = self.CheckMoves(board, moves, thisLocation)
                if hasMove:
                    canMove[piece[0]] = hasMove
        if canMove["b"] and canMove["w"]:
            return False
        if not canMove["b"]: #Return other player's name since they are winner
            return "w"
        if not canMove["w"]:
            return "b"
        return True
    def CheckForWin(self, board):
        #Checks to see if board is empty of one piece
        pieceCount = {'b': 0, 'w':0}
        for row in board.getGrid():
            pieceCount['b'] += row.count('b') + row.count('bk')
            pieceCount['w'] += row.count('w') + row.count('wk')
        if pieceCount['b'] == 0:
            return "w" #Return other player's name since they are winner
        elif pieceCount['w'] == 0:
            return "b"
        else:
            return 0
    def updateToKings(self, board):
        for j in range(8):
            checkB = p.location(0, j)
            checkW = p.location(7, j)
            if board.get(checkB)=="b":
                board.set(checkB, "bk")
            if board.get(checkW)=="w":
                board.set(checkW, "wk")
                
    def updateBoardfromScan(self, board, scanData, currentPlayer):
        #Compares board to scan
        #finds differences and updates board
        #returns false if two pieces different
        pieceToSet = p.location(-1, -1) #Stores the location of the piece to be set to currentPlayer
        oldPieces = list() #Stores the locations of the piece to that need to be removed
        scan = grid.grid(0)
        scan.massSet(scanData)
        pieceTypeToSet = currentPlayer #this gets changed if their is a missing king, therefore piece moved was a king kindof hacky
        for i in range(8):
            for j in range(8):
                currentPos = p.location(i, j)
                if scan.get(currentPos)==1 and not board.get(currentPos)==" ":
                    continue
                elif scan.get(currentPos)==1 and board.get(currentPos)==" ":
                    pieceToSet = currentPos
                elif scan.get(currentPos)==0 and not board.get(currentPos)==" ":
                    if board.get(currentPos)[0] == currentPlayer:
                        pieceTypeToSet = board.get(currentPos) #if the piece removed was of the current player, set that type to be set
                    oldPieces.append(currentPos)
                elif scan.get(currentPos)==0 and board.get(currentPos)==" ":
                    continue
                else:
                    print("ERROR IN SETTING BOARD")
                    return False
        done = board.set(pieceToSet, pieceTypeToSet)
        if done==None:
            print("no move done")
            return False
        for l in oldPieces:
            board.set(l, " ")
        self.updateToKings(board)
        return None
    '''
    b is player 2
    w is player 1
    bk is player 2's kings
    wk is player 1's kings

    '''
    def __init__(self):
        self.scanData = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]
            ]
        self.startingBoard = [
            [" ", "w", " ", "w", " ", "w", " ", "w"],
            ["w", " ", "w", " ", "w", " ", "w", " "],
            [" ", "w", " ", "w", " ", "w", " ", "w"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["b", " ", "b", " ", "b", " ", "b", " "],
            [" ", "b", " ", "b", " ", "b", " ", "b"],
            ["b", " ", "b", " ", "b", " ", "b", " "]
            ]
        self.board = grid.grid(" ")
        self.board.massSet(self.startingBoard) #init board
        self.turnM = t.turnManager(['w','b'])
    def setScanData(self, data): #Shouldn't need to be used but here anyways
        self.scanData = data
    def updateBoard(self, data): #To be called
        self.scanData = data
        temp = self.updateBoardfromScan(self.board, self.scanData, self.turnM.currentPlayer())
        if temp == True:
            print("no updates") #get scan again
            return 0
        elif temp == False:
            print("ERROR") #some error handling here
            return 0
        else:
            #print("Success")
            pass
        return 1
    def getCurrentPlayer(self): #used in the master switcher between ai and human and network
        return self.turnM.currentPlayer()
    def check(self): #Checks if someone has won
        result = self.CheckForWin(self.board)
        if not result == 0:
            print(result, "wins")
            return result
        else:
            result = self.CheckForStalemate(self.board)
            if not result == False:
                print(result, "wins")
                return result
        return None
    def getBoard(self): #DEBUG function
        return self.board
    def nextTurn(self):
        self.turnM.nextTurn()
