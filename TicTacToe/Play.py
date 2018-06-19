import XO
from airand import *
from aismart import *
from aismarter import *
from human import *
from humanNetworked import *
"""
Used to play a single game of checkers includes print statements for human
"""
"""Create the players"""
p1 = AIsmarter("x", "o")
p2 = NetHuman("o", "x")
"""add players to array"""
players = [p1, p2]

def main():
    """Init Game done in here in case of wanting to play again"""
    game = XO.XO(3, players)
    game.start()
    #This should be coming from physical board
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
    userInput = input("Enter r to play again and enter to quit\n")#Wait for keypress to end
    if userInput == "r":
        main() #yes this is bad practice but not likely to hit max recursion in this case
main()
