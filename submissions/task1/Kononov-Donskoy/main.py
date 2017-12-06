import task1 as tsk

import numpy as np
def main():

    #input count of rows
    
    print ('Write count of row.')
    n = int(input())

    #input count of columns
    
    print ('Write count of column.')
    m = int(input())
    
    shape = list()
    shape.append(n)
    shape.append(m)
    matrix = np.zeros(shape)
    
    #input array
    for i in range(n):
        print('Write string №',i,', it include',m,'numbers.')     
        st = input().split()
        for j in range(m):
            matrix[i][j] = float(st[j])

    Res, St1, St2 = tsk.nash_equilibrium(matrix)
    tsk.print_graf(Res, St1, St2)

main()
