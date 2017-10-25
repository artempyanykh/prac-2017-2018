import numpy as np
from scipy.optimize import linprog


def nash_equlibrium(a):
    m, n = a.shape 
    
    #здесь минимизируем со знаком > (lines)
    c = np.ones((m,))
    b_ub = np.ones((n,))
    b_ub = -1 * b_ub
    a_new = -1 * np.transpose(a)
    res1 = linprog(c, A_ub = a_new, b_ub = b_ub)
    v, p = 1.0/res1.fun, res1.x
    p = v * p
    
    #максимизируем со знаком < (columns)
    c2 = np.ones((n,))
    c2 = -1 * c2
    b_ub2 = np.ones((m,))
    res2 = linprog(c2, A_ub = a, b_ub = b_ub2)
    q = res2.x
    q = v * q
    return v, p, q
