import XO
from airand import *
from aismart import *
from human import *

"""Create the players"""
p1 = AIrand("x")
p2 = AIrand("o")
#print("You are 'o'")
"""add players to array"""
players = [p1, p2]

game = XO.XO(3, players)
game.start() #choose starting player

boardState = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

wins = {"x wins": 0, "o wins": 0, "Stalemate":0}
for i in range(1000):
    while True:
        #print(game.currentPlayer(), "turn")
        #game.printBoard()
        move = game.currentPlayer().getMove(game.board)
        boardState[move[0]][move[1]] = 1
        if not game.updateBoard(boardState) == 1:
            #print("Invalid Move")
            continue
        result = game.checkForWin()
        if result:
            #game.printBoard()
            #print("==================")
            #print(result)
            wins[result] += 1
            break
        game.nextTurn()
    #Reset everything
    boardState = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
    game = XO.XO(3, players)
    game.start()
print(wins)
