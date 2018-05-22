import location as p
class grid:
    def __init__(self, default):
        self.grid = [[default for i in range(8)] for j in range(8)]
    def reset(self, default):
        self.grid = [[default for i in range(8)] for j in range(8)]
    def get(self, location):
        if not location.valid():
            return None
        return self.grid[location.row()][location.column()]
    def getRow(self, index):
        return self.grid[index]
    def getGrid(self):
        return self.grid
    def set(self, location, value):
        if not location.valid():
            return None
        self.grid[location.row()][location.column()] = value
        return True
    def massSet(self, values):
        for r in range(8):
            for c in range(8):
                self.grid[r][c] = values[r][c]
    def __repr__(self):
        out = "  "
        for i in range(8):
            out += str(i)
            out += " "
        out += "\n"
        i = 0
        for r in self.grid:
            out += str(i)
            for e in r:
                out += "|" + str(e)
            out += "\n"
            i += 1
        return out
