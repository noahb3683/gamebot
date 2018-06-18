import checkerLogic
import checkers
import location as p
import AIRandom as air
c = checkers.checkers() #Class used in physical board version
sim = checkerLogic.checkerLogic() #Class used to similute physical board
a1 = air.AIRandom("w")
#while c.check()==None:
"""PLAYERS TURN"""

sim.move([p.location(2, 1), p.location(3, 2)])
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())

sim.move([p.location(5, 4), p.location(4, 3)])
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())

sim.move([p.location(6, 5), p.location(5, 4), p.location(4, 5)])
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())

sim.move([p.location(7, 6), p.location(6, 5)])
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())

sim.move(a1.getMove(c.getBoard()))
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())

sim.move([p.location(5, 6), p.location(6, 5)])
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())

sim.move(a1.getMove(c.getBoard()))
c.updateBoard(sim.TFoutput())
c.check()
c.nextTurn()
print(c.getBoard())
"""AI TURN"""

    
c.nextTurn()
