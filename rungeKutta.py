import creator_vectors_and_n


def rungeKutta(f, h, y0, xn, x0):
    x, y, n = creator_vectors_and_n.create_x_y_n(xn, x0, h, y0)
    i = 0
    while i < n:
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k1)
        k3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if y[i+1] > 200000:
            break
        x[i + 1] = x[i] + h
        i += 1
    return x, y
