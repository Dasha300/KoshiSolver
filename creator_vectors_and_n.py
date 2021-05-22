def create_x_y_n(xn, x0, h, y0):
    n = int(round((xn - x0) / h))
    y = []
    for i in range(n + 1):
        y.append(0)
    x = []
    for i in range(n + 1):
        x.append(0)
    y[0] = y0
    x[0] = x0
    return x, y, n
