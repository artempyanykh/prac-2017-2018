import unittest
import numpy as np
import proj

class TestFunc(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
#тест из примера
	def test_number_1(self):

		a = np.array([[4, 0, 6, 2, 2, 1],
					 [3, 8, 4, 10, 4, 4],
					 [1, 2, 6, 5, 0, 0],
					 [6, 6, 4, 4, 10, 3],
					 [10, 4, 6, 4, 0, 9],
					 [10, 7, 0, 7, 9, 8]])
		res1 = np.array([[0, 0.12903226, 0.09677419, 0.43548387, 0.33870968, 0],
		                [0, 0, 0.69086022, 0.14516129, 0.14784946, 0.01612903],
			             4.87096774194])
		res2 = proj.nash_equilibrium(a, True, False)
		
		self.assertAlmostEqual(res1[2], res2[2], 4)
		for i in range(len(res1[0])): 		
			self.assertAlmostEqual(res1[0][i], res2[0][i], 4)
		for i in range(len(res1[1])):			
			self.assertAlmostEqual(res1[1][i], res2[1][i], 4)

#тест для случая, когда спектр оптимальной стратегии состоит из одной точки		
	def test_number_2(self):
		a = np.array([[7, 6, 1, 5],
					 [4, 0, 0, 2],
					 [9, 1, -6, 1],
					 [3, 1, -1, 1]])
		res1 = np.array([[1, 0, 0, 0], [0, 0, 1, 0], 1])
		res2 = proj.nash_equilibrium(a, True, False)
		
		self.assertAlmostEqual(res1[2], res2[2], 4)		
		for i in range(len(res1[0])): 		
			self.assertAlmostEqual(res1[0][i], res2[0][i], 4)
		for i in range(len(res1[1])):			
			self.assertAlmostEqual(res1[1][i], res2[1][i], 4)

#тест для случая, когда спектр оптимальной стратегии неполон	
	def test_number_3(self):
		a  = np.array([[1, 4, 3],
					  [4, 1, 2],
					  [3, 2, 1]])
		res1 = np.array([[0.5, 0.5, 0],
						 [0.5, 0.5, 0],
						  2.5])
		res2 = proj.nash_equilibrium(a, True, False)

		self.assertAlmostEqual(res1[2], res2[2], 4)		
		for i in range(len(res1[0])): 		
			self.assertAlmostEqual(res1[0][i], res2[0][i], 4)
		for i in range(len(res1[1])):			
			self.assertAlmostEqual(res1[1][i], res2[1][i], 4)

#тест для случая, когда спектр оптимальной стратегии полон
	def test_number_4(self):
		a = np.array([[2, -1],
					 [-1, 1]])
		res1 = np.array([[0.4, 0.6], [0.4, 0.6], 0.2])
		res2 = proj.nash_equilibrium(a, True, False)

		for i in range(len(res1[0])): 		
			self.assertAlmostEqual(res1[0][i], res2[0][i], 4)
		for i in range(len(res1[1])):			
			self.assertAlmostEqual(res1[1][i], res2[1][i], 4)

if __name__ == '__main__':
    unittest.main()