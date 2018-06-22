#Task 1 group 311 Kononov, Donskoy

#coding: utf-8

import tkinter
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
    
    #print_graf(V, P, Q)

    return V, P, Q

def print_graf(R, st1, st2):
 
    #printing answer
    
    print('First player strategy: { ', end = '')
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
    
#    figure = plt.figure()
    plt.scatter(range(len(st1)), st1, color = 'blue')
    
    plt.xlabel('First player strategy')
    plt.ylabel('Probability')
    
    plt.title('First strategy')
    plt.grid()  
    plt.show()

#    figure = plt.figure()
    plt.scatter(range(len(st2)), st2, color = 'blue')
    
    plt.xlabel('Second player strategy')
    plt.ylabel('Probability')

    plt.title('Second strategy')
    plt.grid()
    plt.show()
