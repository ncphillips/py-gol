import unittest
from src.gol import World


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
        self.assertEqual(0, world.size())

        world.add_cell(1, 0)
        self.assertEqual(1, world.size())

        world.add_cell(1, 1)
        self.assertEqual(2, world.size())
        self.assertEqual(2, world.size())

    def test_adding_cell_to_location_twice_doesnt_increase_size(self):
        world = World()
        world.add_cell(3, 1)
        world.add_cell(3, 1)
        self.assertEqual(1, world.size())
