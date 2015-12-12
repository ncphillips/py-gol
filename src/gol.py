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
            return True
        return None

class Cell:

    def __init__(self):
        pass

    @staticmethod
    def create_living_cell():
        return Cell()

    def is_alive(self):
        return True