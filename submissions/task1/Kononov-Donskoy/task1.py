#Task 1 group 311 Kononov, Donskoy

# coding: utf-8

import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def nash_equilibrium(A):

    row_c, column_c = A.shape

    #find min element

    addition = 0

    min_elem = np.amin(A)

    if min_elem <= 0:
        addition = abs(min_elem) + 1

    #add to each array element module of min element 

    A = A + addition
    
    ##############################################################

    #Solving first player task

    c1 = np.ones(row_c)                 #coefficients of linear function
    b_ub1 = -1 * np.ones(column_c)      #upper-bound values array

    A_t = (-1) * np.transpose(A)
    result = linprog(c1, A_ub = A_t, b_ub = b_ub1)

    V = 1 / result.fun         #modified funtion value
    P = V * result.x           #original array of solutuin variable

    ##############################################################

    #Solving second player task

    c2 = (-1) * np.ones(column_c)       #coefficients of linear function
    b_ub2 = np.ones(row_c)              #upper-bound values array

    result = linprog(c2, A_ub = A, b_ub = b_ub2)

    V = - (1 / result.fun)      #modified funtion value
    Q = V * result.x            #original array of solutuin variable

    V -= addition               #original function value

    ##############################################################
    
    print_plot(V, P, Q)

def print_plot(R, st1, st2):
 
    #printing answer
    
    print('First player strategy: { ')
    for i in range(len(st1)):
        print( "%.3f" % st1[i], end = '')
        if i!=len(st1)-1:
            print(' ; ', end = '')
        else:
            print('}')

    print('Second player strategy: { ', end = '')
    for i in range(len(st2)):
        print( "%.3f" % st2[i], end = '')
        if i!=len(st2)-1:
            print(' ; ', end = '')
        else:
            print('}')

    print("Solution: %.3f \n"  % R)
    
    figure = plt.figure()
    plt.scatter(range(1, len(st1) + 1), st1, color = 'blue')
    
    plt.xlabel('First player strategy')
    plt.ylabel('Probability')
    
    plt.grid()
    plt.show()

    figure = plt.figure()
    plt.scatter(range(1, len(st2) + 1), st2, color = 'blue')
    
    plt.xlabel('Second player strategy')
    plt.ylabel('Probability')

    plt.grid()
    plt.show()

def main():

    m = 4
    n = 3

    #input count of rows
    '''
    print ('Write count of row.')
    m = int(input())

    #input count of columns
    print ('Write count of column.')
    n = int(input())
    '''

    #input array
    '''for i in range(n):
        print('Write string №',i,', it include',m,'numbers.')     
        st = input().split()
        for j in range(m):
            matrix[i][j] = float(st[j])
    '''
    #Example:
    matrix =np.array([[5,6,3,0],[10,5,12,10],[10,0,5,20]])
    nash_equilibrium(matrix)

main()
