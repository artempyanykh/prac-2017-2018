from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt
import random
import sys


# основная функция, производящая расчеты
def nash_equilibrium(a, ret = False, show = True):
	matrix_min = find_matrix_min(a)
	a += matrix_min	
	a_minus = -1 * a
	res1 = linprog(np.ones(len(a)), a_minus.transpose(), np.linspace(-1, -1, len(a[0])))
	value = 1/res1.fun 
	strat1 = value * np.array(res1.x) 
	res2 = linprog(np.linspace(-1, -1, len(a[0])), a, np.ones(len(a)))
	strat2 = value * np.array(res2.x)
	value -= matrix_min	
	res = np.array([strat1, strat2, value])
	if show:
		print("value = ", res[2])
		print("p = ", res[0])
		print("q = ", res[1])
		print_graph(res[0], res[1])
	if ret:	
		return res

# функция находит число, которое нужно прибавить к матрице 
def find_matrix_min(a):
	min_val = a.min()
	if min_val > 0:
		return 0
	return abs(min_val) + 1


# функция выводит на экран спектры оптимальных стратегий игроков, и сохраняет их в формате png 
def print_graph(strat1,strat2):
	x = np.arange(1, len(strat1) + 1, 1)
	plt.figure(1)
	plt.title("Strategy of the first player")
	plt.grid(linestyle='solid')	
	plt.plot(x, strat1, 'go')
	plt.show()

	x = np.arange(1, len(strat2) + 1, 1)
	plt.figure(2)
	plt.title("Strategy of the second player")
	plt.grid(linestyle='solid')	
	plt.plot(x, strat2, 'bo')
	plt.show()

# генерация рандомной матрицы
def random_matrix():
	s = random.randint(1,20)
	c = random.randint(1,20)
	matrix = np.empty((s, c))
	for i in range(s):
		for j in range(c):
			matrix[i][j] = random.randint(-100, 100)
			print(matrix[i][j], " ",  end="")
		print('\n')
	return matrix

# чтение матрицы из файла
def matrix_from_file(name):
	with open(name, 'r') as ifile:
		size_line = len((ifile.readline()).split())
	matrix = np.loadtxt(name, usecols=range(size_line))
	return matrix	