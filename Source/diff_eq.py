import numpy as np
import functions as f
from scipy.integrate import solve_ivp

# Метод Эйлера


def euler(func, a, b, y0, n):

    h = (b - a) / n
    x = a
    y = np.array(y0, dtype=float)
    xs, ys = [x], [y.copy()]

    for i in range(n):
        y += h * func(x, y)
        x += h
        xs.append(x)
        ys.append(y.copy())

    return np.array(xs), np.array(ys)


# Метод Рунге-Кута


def runge(func, a, b, y0, n):
    h = (b - a) / n
    x = a
    y = np.array(y0, dtype=float)
    xs, ys = [x], [y.copy()]

    for i in range(n):
        k1 = h * func(x, y)
        k2 = h * func(x + h / 2, y + k1 / 2)
        k3 = h * func(x + h / 2, y + k2 / 2)
        k4 = h * func(x + h, y + k3)

        f_i = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        y += f_i
        x += h

        ys.append(y.copy())
        xs.append(x)

    return np.array(xs), np.array(ys)
