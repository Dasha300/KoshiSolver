def Adams_Bashforth_euler(f, h, y0, xn, x0):
    eps = int(round((xn - x0) / h))
    y = []
    for i in range(eps + 1):
        y.append(0)
    x = []
    for i in range(eps + 1):
        x.append(0)
    y[0] = y0
    x[0] = 0
    i = 1
    y[1] = y[0] + h * f(x[0], y[0])
    x[1] = x[0] + h
    while i < eps:
        y[i + 1] = y[i] + 3 / 2 * h * f(x[i], y[i]) - 1 / 2 * h * f(x[i - 1], y[i - 1])
        x[i + 1] = x[i] + h
        i += 1
    return x, y
