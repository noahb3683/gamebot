import XO
from airand import *
from human import *

"""Create the players"""
p1 = AIrand("x")
p2 = Human("o")
print("You are 'o'")
"""add players to array"""
players = [p1, p2]

game = XO.XO(3, players)
game.start() #choose starting player

boardState = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
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
    
