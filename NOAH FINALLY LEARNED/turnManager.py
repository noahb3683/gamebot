import random
class turnManager:
    def __init__(self, turns):
        self.currentTurn = turns[0]
        self.numberOfTurns = len(turns)
        self.currentTurnNum = 0
        self.turns = turns
        self.turnCount = 0
    def currentPlayer(self):
        return self.currentTurn
    def nextTurn(self):
        self.currentTurnNum += 1
        self.turnCount += 1
        self.currentTurnNum = self.currentTurnNum%self.numberOfTurns
        #if self.currentTurnNum >= self.numberOfTurns:
        #    self.currentTurnNum = 0
        self.currentTurn = self.turns[self.currentTurnNum]
    def numberOfTurns(self):
        return self.turnCount
    def randomizePlayer(self):
        self.currentTurnNum = round(random.uniform(0, self.numberOfTurns-1))
        self.currentTurn = self.turns[self.currentTurnNum]
