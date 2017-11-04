import unittest
import numpy as np
from code.nash import nash_equilibrium
class Test_Equilibrium(unittest.TestCase):
    def test_1(self):
        game_price, strategy1, strategy2 = nash_equilibrium([[0, 0],[0, 0]])
        self.assertEqual(game_price, 0)
        np.testing.assert_array_equal([[1, 0], [1, 0]], [strategy1, strategy2])
