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


        all_neighbours = set()
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                all_neighbours.add((i,j))

        # a cell isn't a neighbour of itself
        all_neighbours.remove((x, y))

        for neighbour in all_neighbours:
            if neighbour in self.cells:
                neighbours += 1

        return neighbours

    def tick(self):
        self.cells = set()
        return self.cells

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

    # you're a barbarian with your function naming, nolan
    def willBeAlive(self, num_neighbours):
        return self.will_be_alive(num_neighbours)

    def will_be_alive(self, num_neighbours):
        if self.living:
            return (num_neighbours == 2 or num_neighbours == 3)
        return num_neighbours == 3
