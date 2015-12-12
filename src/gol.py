class World:

    def __init__(self):
        self.cells = []
        pass

    def size(self):
        return len(self.cells) - 1

    def empty(self):
        return len(self.cells) == 0

    def add_cell(self, x, y):
        self.cells.append((x, y))
