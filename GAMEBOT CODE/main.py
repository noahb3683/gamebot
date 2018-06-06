import checkerLogic
import checkers
import location as p
import AIRandom as air
c = checkers.checkers() #Class used in physical board version
sim = checkerLogic.checkerLogic(c.getBoard()) #Class used to similute physical board
a1 = air.AIRandom("w")
print(a1.getMove(c.getBoard()))
#while c.check()==None:
"""PLAYERS TURN"""

sim.move([p.location(2, 1), p.location(3, 2)])
print(c.getBoard())

sim.move([p.location(5, 4), p.location(4, 3)])
print(c.getBoard())
sim.move([p.location(3, 2), p.location(5, 4), p.location(4,5)])
#sim.move([p.location(1, 0), p.location(3, 2)])
#sim.move([p.location(1, 0), p.location(3, 2)])
print(c.getBoard())
"""AI TURN"""

    
c.nextTurn()
