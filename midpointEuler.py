def midpoint_euler(f, h, y0, xn, x0):
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
        y[i + 1] = y[i] + h * f(x[i] + 1 / 2 * h, y[i] + 1 / 2 * h * f(x[i], y[i]))
        if y[i+1] > 200000:
            break
        x[i + 1] = x[i] + h
        i += 1
    return x, y
