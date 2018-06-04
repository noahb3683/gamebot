import location as p
import grid
import numpy as np
"""
Trys to simulate physical board
Used to play checkers without the board for testing the AI
Sketchy because it needs to output board to true/false table to properly test all the code
"""
class checkerLogic:
    def __init__(self, startingConfig):
        self.realBoard = startingConfig
    def TFoutput(self): #Converts board into T/F table to simulate board
        output = [[0 for i in range(8)] for j in range(8)]
        for i in self.realBoard.getGrid():
            for j in i:
                if not j==" ":
                    output[i][j]=1
        return output
    def updateBoard(self, board): #Updates copy of board, shouldn't be needed
        self.realBoard = board
    def move(self, moves):#location of peice to move from to each spot in array, removes pieces in way
        if len(moves) < 2:
            #Not enough moves entered
            return 0
        peice = self.realBoard.get(moves[0]) #gets peice that is moving
        startingLocation = moves[0]
        for i in range(1, len(moves)): #to account for starting move
            currentLocation = moves[i]
            direction = np.array(currentLocation-startingLocation)//2 
            checkLocation = p.location(currentLocation-p.location(direction)) #Location of piece hopped over

            if not self.realBoard.get(startingLocation)[0] == self.realBoard.get(checkLocation)[0]:
                self.realBoard.set(checkLocation, " ") #set blank if not of the same type as piece moved
            self.realBoard.set(startingLocation, " ") #Set old spot blank
            self.realBoard.set(currentLocation, peice) #Set new spot with piece
            startingLocation = currentLocation #Update for next tick
        print(self.realBoard)
