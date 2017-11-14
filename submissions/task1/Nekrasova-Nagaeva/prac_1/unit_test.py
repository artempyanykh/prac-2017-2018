from matrix_game.nash_equilibrium import nash_equilibrium
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import unittest

def test_1():
    fin = 'in/test_1.in'
    a = np.loadtxt(fin, dtype = 'float64')
    v = 9 / 5
    sa = np.array([2 / 5, 2 / 5, 1 / 5])
    sol = nash_equilibrium(a)
    b = abs(sol[0] - v) < 0.001
    if b == False:
        assert b
    i = 0
    for c in sa:
        if abs(sol[1][i] - c) > 0.001:
            b = False
        if abs(sol[2][i] - c) > 0.001:
            b = False
        if b == False:
            break
        i += 1
    assert b

def test_2():
    fin = 'in/test_2.in'
    a = np.loadtxt(fin, dtype='float64')
    v = 18 / 7
    sa = np.array([3 / 7, 4 / 7])
    sb = np.array([2 / 7, 5 / 7])
    sol = nash_equilibrium(a)
    b = abs(sol[0] - v) < 0.001
    if b == False:
        assert b
    i = 0
    while i < 2:
        if abs(sol[1][i] - sa[i]) > 0.001:
            b = False
        if abs(sol[2][i] - sb[i]) > 0.001:
            b = False
        if b == False:
            break
        i += 1
    assert b

def test_3():
    fin = 'in/test_3.in'
    a = np.loadtxt(fin, dtype='float64')
    v = 151 / 31
    sa = np.array([0, 4/31, 3/31, 27/62, 21/62, 0])
    sb = np.array([0, 0, 257/372, 9/62, 55/372, 1/62])
    sol = nash_equilibrium(a)
    b = abs(sol[0] - v) < 0.001
    if b == False:
        assert b
    i = 0
    while i < 6:
        if abs(sol[1][i] - sa[i]) > 0.001:
            b = False
        if abs(sol[2][i] - sb[i]) > 0.001:
            b = False
        if b == False:
            break
        i += 1
    assert b
