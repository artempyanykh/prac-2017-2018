import numpy as np
from scipy.optimize import linprog


def nash_equilibrium(in_matrix):
    a = np.matrix(in_matrix)
    n = len(a)

    row_min = np.min(a, 1)
    col_max = np.max(a.T, 1)

    for i in range(0, n):
        for j in range(0, n):
            if (a[i, j] == row_min[i] and a[i, j] == col_max[j]):
                p = np.zeros(n)
                q = np.zeros(n)
                p[i] = 1
                q[j] = 1
                return {'f': a[i, j], 'p': p.tolist(), 'q': q.tolist()}

    add = min(0, np.min(a))
    a -= add

    c = np.ones(n)
    a_ub = np.vstack((-a.T, -np.identity(n)))
    b_ub = np.hstack((np.full(n, -1), np.zeros(n)))

    res = linprog(c, a_ub, b_ub)
    f = 1 / res.fun + add
    p = res.x * res.fun

    c = np.full(n, -1)
    a_ub = np.vstack((a, -np.identity(n)))
    b_ub = np.hstack((np.ones(n), np.zeros(n)))

    res = linprog(c, a_ub, b_ub)
    q = res.x * -res.fun

    return {'f': f, 'p': p.tolist(), 'q': q.tolist()}
