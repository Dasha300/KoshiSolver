import creator_vectors_and_n


def backward_euler(f, h, y0, xn, x0):
    x, y, n = creator_vectors_and_n.create_x_y_n(xn, x0, h, y0)
    i = 0
    while i < n:
        z = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * f(x[i + 1], z)
        if y[i+1] > 200000:
            break
        i += 1
    return x, y
