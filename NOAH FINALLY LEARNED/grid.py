import location as p
board_size = 3
class grid:
    def __init__(self, default, board_size=3):
        self.board_size = 3
        self.grid = [[default for i in range(self.board_size)] for j in range(self.board_size)]
    def reset(self, default):
        self.grid = [[default for i in range(self.board_size)] for j in range(self.board_size)]
    def get(self, location):
        if not location.valid():
            return None
        return self.grid[location.row()][location.column()]
    def getRow(self, index):
        return self.grid[index]
    def getGrid(self):
        return self.grid
    def getSize(self):
        return self.board_size
    def set(self, location, value):
        if not location.valid():
            return None
        self.grid[location.row()][location.column()] = value
        return True
    def __iter__(self):
        for row in self.grid:
            yield row        
    def massSet(self, values):
        for r in range(self.board_size):
            for c in range(self.board_size):
                self.grid[r][c] = values[r][c]
    def __repr__(self):
        out = "  "
        for i in range(self.board_size):
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
