from unittest import TestCase
import numpy as np
import nash

class TestNashEquilibrium(TestCase):
    def test_answers(self):
        v, p, q = nash.nash_equlibrium(np.array([[1, 4], [3, 2]]))
        np.testing.assert_array_almost_equal([0.25, 0.75], p)
        np.testing.assert_array_almost_equal([0.5, 0.5], q)
    def another_test(self):
        v, p, q = nash.nash_equlibrium(np.array([[1, 1], [3, 1]]))
        self.assertAlmostEqual(v, 1)
        np.testing.assert_array_almost_equal([1, 0], p)
        np.testing.assert_array_almost_equal([0, 1], q)
        
