import numpy as np
from scipy.optimize import linprog

def nash_equilibrium(a):
  M = 0
  if a.min() <= 0:                            # Сделаем все элементы матрицы неотрицательными,
    M = abs(a.min())                          # так как это не влияет на процесс поиска решения
    a += M
  m = a.shape[0]                              # размеры матрицы (m*n)
  n = a.shape[1]

  c = np.ones((m))                            # необходимо минимизировать F = x1+...+xm = 1/V
  A_ub = -a.T                                 # сводим к неравенствам ≤ домножением матрицы и
  b_ub = -np.ones((n))                        # правой части на (-1)
                                    
  res = linprog(c, A_ub, b_ub)                # с помощью функции linprog полчаем
                                              # решение задачи:
                                              #   𝑐𝑇*𝑥 → 𝑚𝑖𝑛
                                              #   𝐴_𝑢𝑏*𝑥 ≤ 𝑏_𝑢𝑏 
                                              #   𝐴_𝑒𝑞*𝑥 = 𝑏_𝑒𝑞 
                                              #   𝑥 ≥ 0
  V = 1/res.fun - M   
  first_str = 1/res.fun * res.x                       
                                              
  c = -np.ones((n))                           # необходимо максимизировать F = y1+...yn = 1/V
  A_ub = a                                    # сведем задачу к задаче минимизации 
  b_ub = np.ones((m)) 
  res = linprog(c, A_ub, b_ub)
  second_str = (-1/res.fun) * res.x
  return V, first_str, second_str
