import unittest
from src.gol import World


class WorldTest(unittest.TestCase):
    def test_new_world_is_empty(self):
        world = World()
        self.assertEqual(0, world.size())
