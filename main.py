import matplotlib.pyplot as plt
import euler
import backwardEuler
import AdamsBashford
import rungeKutta
import numpy as np


def f(x, y):
    return y * 2 + x+2


x, y = euler.euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x1, y1 = backwardEuler.backward_euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x2, y2 = AdamsBashford.Adams_Bashforth_euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x3, y3 = rungeKutta.rungeKutta(f=f, h=0.1, y0=0, xn=1, x0=0)
fig = plt.figure()
y4 = [1 / 4 * (5 * np.exp(2 * i) - 5 - 2 * i) for i in x]
l1, l2, l3, l4, l5,  = plt.plot(x, y, x1, y1, x2, y2, x3, y3, x, y4)
fig.legend((l1, l2, l3, l4, l5),('Euler', 'Backward Euler', 'Adams-Bashforth Euler', 'Runge Kutta', 'Exact Solution'))
plt.show()
