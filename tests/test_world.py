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

    def test_getting_cell_returns_not_none(self):
        world = World()
        world.add_cell(0, 1)
        cell = world.get_cell(0, 1)
        self.assertTrue(cell.is_alive())


class CellTests(unittest.TestCase):
    def test_living_cell_is_alive(self):
        cell = Cell.create_living_cell()
        self.assertTrue(cell.is_alive())

    def test_dead_cell_is_dead(self):
        cell = Cell.create_dead_cell()
        self.assertFalse(cell.is_alive())