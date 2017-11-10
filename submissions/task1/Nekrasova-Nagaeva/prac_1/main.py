import sys
import numpy as np
from matrix_game import nash_equilibrium, graph

def main(fin, fout):
    H = np.loadtxt(fin, dtype='float64')
    f = open(fout, 'w')
    print(H)
    sol = nash_equilibrium(H)
    print ("Выигрыш равен: ", sol[0])                
    print ("Стратегия первого игрока: ", sol[1])
    print ("Стратегия второго игрока: ", sol[2])
    f.write("%f\n" %sol[0])
    for c in sol[1]:
      f.write("%f " %c)
    f.write("\n")
    for c in sol[2]:
      f.write("%f " %c)
    graph(sol[1], sol[2])

