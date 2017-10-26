import numpy as np 
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def nash_equilibrium(A): #поиск равновесия Нэша
     p1 = [ ] ##первый игрок
     p2 = [ ] ##второй игрок
     count = 0 
     ##коэффициенты для задачи линейного програмиирования
     line1 = [ ]
     line2 = [ ]
     koef1 = [ ]
     koef2 = [ ]
     m = A.shape[0] ##столбцы матрицы
     n = A.shape[1] ##cтроки матрицы

     mmin = np.amin(A)
     if (mmin <= 0):
          A = A + abs(mmin) + 1 
     else:
          count = count + mmin - 1 
     
     Atr = -A.transpose() ##транспонированная матрица
     line1 = -np.ones(n)
     koef1 = np.ones(m)
     line2 = np.ones(m)
     koef2 = -np.ones(n)
     
     matrix = linprog(line1, A_ub = A, b_ub = koef1)
     p2 = matrix.get("x")
     matrix = linprog(line2, A_ub = Atr, b_ub = koef2)
     p1 = matrix.get("x")
     count = 1 / np.sum(p1)
     p1 = p1 * count
     p2 = p2 * count
     
     print ("стратегия первого игрока: ", p1)
     print ("стратегия второго игрока: ", p2)
     print ("Игровая сумма: ", count)
     return p1, p2, count

def art(p,q): #рисовка гистограммы 
     f1 = [ ]
     for i in range (len(p)):
          f1.append(i)
     st = plt.figure()
     plt.bar(f1, p)
     plt.title("стратегия 1 игрока: ")
     plt.xlabel('Стратегия')
     plt.ylabel('Вероятность')
     plt.xlim(0,len(p))
     plt.ylim(0, np.max(p)+1)
     
     f2 = [ ]
     for i in range (len(q)):
          f2.append(i)
     st = plt.figure()
     plt.bar(f2, p)
     plt.title("стратегия 2 игрока: ")
     plt.xlabel('Стратегия')
     plt.ylabel('Вероятность')
     plt.xlim(0,len(q))
     plt.ylim(0, np.max(q)+1)
     plt.show()
     
a = np.array([[3, 9, 2, 1, 1], 
              [7, 8, 5, 6, 8], 
              [4, 7, 3, 5, 7], 
              [5, 6, 1, 7, 7],
              [6, 7, 1, 4, 5]])
b = nash_equilibrium(a)
art(b[0], b[1])

a = np.array([[4,0,6,2,2,1],
              [3,8,4,10,4,4],
              [1,2,6,5,0,0],
              [6,6,4,4,10,3],
              [10,4,6,4,0,9],
              [10,7,0,7,9,8]])
b = nash_equilibrium(a)
art(b[0], b[1])

a = np.array([[1, 2, 3, 4], 
              [2, 3, 4, 1],
              [3, 4, 1, 2], 
              [4, 1, 2, 3]])
b = nash_equilibrium(a)
art(b[0], b[1])
