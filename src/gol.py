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

    def count_neighbours_of(self, x, y):
        neighbours = 0

        for cell in self.cells:
            if (cell[1] - 1) == y or (cell[1] + 1) == y:
                neighbours += 1

        for cell in self.cells:
            if (cell[0] - 1) == x or (cell[0] + 1) == x:
                neighbours += 1
        return neighbours

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
