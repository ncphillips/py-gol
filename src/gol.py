class World:

    def __init__(self):
        self.cells = set()

    def size(self):
        return len(self.cells)

    def empty(self):
        return len(self.cells) == 0

    def add_cell(self, x, y):
        self.cells.add((x, y))

    def get_cell(self, x, y):
        if (x, y) in self.cells:
            return Cell.create_living_cell()
        return Cell.create_dead_cell()

class Cell:

    def __init__(self, alive):
        self.living = alive

    @staticmethod
    def create_living_cell():
        return Cell(True)

    @staticmethod
    def create_dead_cell():
        return Cell(False)

    def is_alive(self):
        return self.living
