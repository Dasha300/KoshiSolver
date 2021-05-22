import creator_vectors_and_n


def midpoint_euler(f, h, y0, xn, x0):
    x, y, n = creator_vectors_and_n.create_x_y_n(xn, x0, h, y0)
    i = 0
    while i < n:
        y[i + 1] = y[i] + h * f(x[i] + 1 / 2 * h, y[i] + 1 / 2 * h * f(x[i], y[i]))
        if y[i+1] > 200000:
            break
        x[i + 1] = x[i] + h
        i += 1
    return x, y
