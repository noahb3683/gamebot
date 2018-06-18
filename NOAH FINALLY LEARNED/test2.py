import XO
from airand import *
from aismart import *
from aismarter import *
from human import *

import time
start_time = time.time()
'''
Allows for two players to play multiple games at once
Does NOT print board
Just prints stats of win record at end of game
'''
"""Create the players"""
p1 = AIsmart("x", "o")
p2 = AIrand("o", "x")
"""add players to array"""
players = [p1, p2]

game = XO.XO(4, players)
game.start() #choose starting player

boardState = [[0 for i in range(game.board_size)] for j in range(game.board_size)]

wins = {"x wins": 0, "o wins": 0, "Stalemate":0}
total_games = 10
for i in range(1,total_games+1):
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
    if i%2 == 0:
        print("done", i, "games")

for key, value in wins.items():
    print(key, value/total_games*100,"%")
print(total_games, "were played")

print("this took %s seconds" % (time.time() - start_time))
