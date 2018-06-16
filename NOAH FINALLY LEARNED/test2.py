import XO
from airand import *
from aismart import *
from human import *

import time
start_time = time.time()
'''
Allows for two players to play multiple games at once
Does NOT print board
Just prints stats of win record at end of game
'''
"""Create the players"""
p1 = AIrand("x", "o")
p2 = AIsmart("o", "x")
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
total_games = 1000
for i in range(total_games):
    while True:
        move = game.currentPlayer().getMove(game.board)
        boardState[move[0]][move[1]] = 1
        if not game.updateBoard(boardState) == 1:
            #if move is invalid get it to try again
            continue
        result = game.checkForWin()
        if result:
            wins[result] += 1
            break
        game.nextTurn()
    #Reset everything
    #game.printBoard()
    boardState = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
    game = XO.XO(3, players)
    game.start()

for key, value in wins.items():
    print(key, value/total_games,"%")
print(total_games, "were played")

print("this took %s seconds" % (time.time() - start_time))
