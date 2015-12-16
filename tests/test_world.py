import unittest
from src.gol import *


class WorldTest(unittest.TestCase):
    def test_new_world_is_empty(self):
        world = World()
        self.assertTrue(world.empty())

    def test_a_world_with_a_cell_is_not_empty(self):
        world = World()
        world.add_cell(0, 0)
        self.assertFalse(world.empty())

    def test_world_size_corresponds_to_num_cells_added(self):
        world = World()

        world.add_cell(0, 0)
        self.assertEqual(1, world.size())

        world.add_cell(1, 0)
        self.assertEqual(2, world.size())

        world.add_cell(1, 1)
        self.assertEqual(3, world.size())
        self.assertEqual(3, world.size())

    def test_adding_cell_to_location_twice_doesnt_increase_size(self):
        world = World()
        world.add_cell(3, 1)
        world.add_cell(3, 1)
        world.add_cell(3, 1)
        self.assertEqual(1, world.size())

    def test_getting_cell_from_empty_location_returns_dead_cell(self):
        world = World()
        cell = world.get_cell(5, 2)
        self.assertFalse(cell.is_alive())

    def test_getting_cell_returns_living_cell(self):
        world = World()
        world.add_cell(0, 1)
        cell = world.get_cell(0, 1)
        self.assertTrue(cell.is_alive())

    def test_count_living_neighbours_of_location_vertical_plane(self):
        world = World()

        world.add_cell(0, 0)
        world.add_cell(0, 1)
        world.add_cell(0, 2)
        world.add_cell(10, 10)

        self.assertEqual(1, world.count_neighbours_of(0, 0))
        self.assertEqual(2, world.count_neighbours_of(0, 1))
        self.assertEqual(1, world.count_neighbours_of(0, 2))
        self.assertEqual(0, world.count_neighbours_of(100, 10))

    def test_count_living_neighbours_of_location_horizontal_plane(self):
        world = World()

        world.add_cell(0, 0)
        world.add_cell(1, 0)
        world.add_cell(2, 0)
        world.add_cell(-10, 10)

        self.assertEqual(1, world.count_neighbours_of(0, 0))
        self.assertEqual(2, world.count_neighbours_of(1, 0))
        self.assertEqual(1, world.count_neighbours_of(2, 0))
        self.assertEqual(0, world.count_neighbours_of(-10, 10))
        self.assertEqual(0, world.count_neighbours_of(100, 10))

    def test_here___diagonally_up(self):
        world = World()

        world.add_cell(0, 0)
        world.add_cell(1, 1)
        world.add_cell(2, 2)
        world.add_cell(-10, 10)

        self.assertEqual(1, world.count_neighbours_of(0, 0))
        self.assertEqual(2, world.count_neighbours_of(1, 1))
        self.assertEqual(1, world.count_neighbours_of(2, 2))
        self.assertEqual(0, world.count_neighbours_of(-10, 10))
        self.assertEqual(0, world.count_neighbours_of(100, 10))

    def test_here___diagonally_down(self):
        world = World()

        world.add_cell(0, 0)
        world.add_cell(-1, -1)
        world.add_cell(-2, -2)
        world.add_cell(-10, -10)

        self.assertEqual(1, world.count_neighbours_of(0, 0))
        self.assertEqual(2, world.count_neighbours_of(-1, -1))
        self.assertEqual(1, world.count_neighbours_of(-2, -2))
        self.assertEqual(0, world.count_neighbours_of(-10, 10))
        self.assertEqual(0, world.count_neighbours_of(78, 13))


class CellTests(unittest.TestCase):
    def test_living_cell_is_alive(self):
        cell = Cell.create_living_cell()
        self.assertTrue(cell.is_alive())

    def test_dead_cell_is_dead(self):
        cell = Cell.create_dead_cell()
        self.assertFalse(cell.is_alive())

    def test_living_cell_with_less_than_2_neighbors_will_not_be_alive(self):
        cell = Cell.create_living_cell()

        for num_neighbours in range(0, 2):
            self.assertFalse(cell.will_be_alive(num_neighbours))

    def test_living_cell_with_2_or_3_neighbours_will_be_alive(self):
        cell = Cell.create_living_cell()

        for num_neighbours in range(2, 4):
            self.assertTrue(cell.will_be_alive(num_neighbours))

    def test_living_cell_with_more_than_3_neighbours_will_not_be_alive(self):
        cell = Cell.create_living_cell()

        for num_neighbours in range(4, 9):
            self.assertFalse(cell.will_be_alive(num_neighbours))

    def test_dead_cell_with_3_neighbours_will_be_alive(self):
        cell = Cell.create_living_cell()

        num_neighbours = 3

        self.assertTrue(cell.will_be_alive(num_neighbours))

    def test_dead_cell_with_less_than_3_neighbours_will_not_be_alive(self):
        cell = Cell.create_dead_cell()

        for num_neighbours in range(0, 3):
            self.assertFalse(cell.will_be_alive(num_neighbours))

    def test_dead_cell_with_more_than_3_neighbours_will_not_be_alive(self):
        cell = Cell.create_dead_cell()

        for num_neighbours in range(4, 9):
            self.assertFalse(cell.will_be_alive(num_neighbours))



