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
