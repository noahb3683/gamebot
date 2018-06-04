import checkerLogic
import checkers
import location as p
c = checkers.checkers() #Class used in physical board version
r = checkerLogic.checkerLogic(c.getBoard()) #Class used to similute physical board

#while c.check()==None:
"""PLAYERS TURN"""

r.move([p.location(1, 0), p.location(3, 2)])


r.move([p.location(1, 0), p.location(3, 2)])
r.move([p.location(1, 0), p.location(3, 2)])
r.move([p.location(1, 0), p.location(3, 2)])
r.move([p.location(1, 0), p.location(3, 2)])
"""AI TURN"""

    
c.nextTurn()
