"""
Class to store locations on grid
includes subtraction and addition
and validitation for checkers board
"""
class location:
    def __init__(self, r, c=0):
        if type(r) is int:
            self.r = r
            self.c = c
        elif type(r) is location:
            self.r = r.r
            self.c = r.c
        else:
            self.r = r[0]
            self.c = r[1]
        self.count = 0 #counts number of times its updated
    def row(self):
        return self.r
    def column(self):
        return self.c
    def pos(self):
        return [self.r, self.c]
    def updateCount(self):
        return self.count
    def updateRow(self,r):
        self.r = r
        self.count += 1
    def updateColumn(self,c):
        self.c = c
        self.count += 1
    def updatePos(self,pos):
        self.r = pos[0]
        self.c = pos[1]
        self.count += 1
    def update(self,r, c):
        self.r = r
        self.c = c
        self.count += 1
    def __sub__(self, other):#Returns r,c list since vector like
        r = self.r-other.r
        c = self.c-other.c
        return [r,c]
    def __radd__(self, other):#adds r,c list as vector
        r = self.r+other[0]
        c = self.c+other[1]
        return location(r, c)
    def __add__(self, other):#adds r,c list as vector
        r = self.r+other[0]
        c = self.c+other[1]
        return location(r, c)
    def valid(self):
        if self.r > 7 or self.r < 0:
            return False
        if self.c > 7 or self.c < 0:
            return False
        return True
    def __repr__(self):
        return "row: %i column: %i" % (self.r, self.c) 
