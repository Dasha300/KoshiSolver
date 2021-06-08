import matplotlib.pyplot as plt
import euler
import backwardEuler
import midpointEuler
import AdamsBashford
import rungeKutta
import numpy as np


def f(x, y):
    return y * 2 + x+2


x, y = euler.euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x1, y1 = backwardEuler.backward_euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x2, y2 = midpointEuler.midpoint_euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x3, y3 = AdamsBashford.Adams_Bashforth_euler(f=f, h=0.1, y0=0, xn=1, x0=0)
x4, y4 = rungeKutta.rungeKutta(f=f, h=0.1, y0=0, xn=1, x0=0)
fig = plt.figure()
y5 = [1 / 4 * (5 * np.exp(2 * i) - 5 - 2 * i) for i in x2]
l1, l2, l3, l4, l5, l6 = plt.plot(x, y, x1, y1, x2, y2, x3, y3, x4, y4, x, y5)
fig.legend((l1, l2, l3, l4, l5, l6),('Euler', 'Backward Euler', 'Midpoint Euler', 'Adams-Bashforth Euler', 'Runge Kutta', 'Exact Solution'))
plt.show()
