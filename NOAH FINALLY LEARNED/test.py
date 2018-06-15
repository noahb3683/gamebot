import XO

game = XO.XO(3)
game.start()

boardState = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
while True:
    print(game.currentPlayer(), "turn")
    game.printBoard()
    x = int(input())
    y = int(input())
    boardState[x][y] = 1
    print(boardState)
    if not game.updateBoard(boardState) == 1:
        continue
    result = game.checkForWin()
    if result:
        print(result)
        break
    game.nextTurn()
    
