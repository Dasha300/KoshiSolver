import creator_vectors_and_n


def Adams_Bashforth_euler(f, h, y0, xn, x0):
    x, y, n = creator_vectors_and_n.create_x_y_n(xn, x0, h, y0)
    i = 1
    y[1] = y[0] + h * f(x[0], y[0])
    x[1] = x[0] + h
    while i < n:
        y[i + 1] = y[i] + 3 / 2 * h * f(x[i], y[i]) - 1 / 2 * h * f(x[i - 1], y[i - 1])
        if y[i+1] > 200000:
            break
        x[i + 1] = x[i] + h
        i += 1
    return x, y
