import XO
from airand import *
from aismart import *
from aismarter import *
from human import *

"""Create the players"""
p1 = AIsmart("x", "o")
p2 = Human("o", "x")
#print("You are 'o'")
"""add players to array"""
players = [p1, p2]

game = XO.XO(4, players)
game.start() #choose starting player

boardState = [[0 for i in range(game.board_size)] for j in range(game.board_size)]
while True:
    print(game.currentPlayer(), "turn")
    game.printBoard()
    move = game.currentPlayer().getMove(game.board)
    boardState[move[0]][move[1]] = 1
    if not game.updateBoard(boardState) == 1:
        print("Invalid Move")
        continue
    result = game.checkForWin()
    if result:
        game.printBoard()
        print("==================")
        print(result)
        break
    game.nextTurn()
    
