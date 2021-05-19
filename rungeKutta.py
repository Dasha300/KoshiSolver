def rungeKutta(f, h, y0, xn, x0):
    eps = int(round((xn - x0) / h))
    y = []
    for i in range(eps + 1):
        y.append(0)
    x = []
    for i in range(eps + 1):
        x.append(0)
    y[0] = y0
    x[0] = 0
    i = 0
    while i < eps:
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k1)
        k3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x[i + 1] = x[i] + h
        i += 1
    return x, y
