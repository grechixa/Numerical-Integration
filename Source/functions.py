import numpy as np


def f(x):
    return np.sqrt(2 * x + 1.6) / (1.8 + np.sqrt(0.3 * x**2 + 2.3))


def g(x, y):
    return (x**2 + y) / (1 + x + y**2)


def control_case_1(x, y):
    return y * (1 - x)


def control_case_2(x, y_vec):
    u, v = y_vec
    du_dx = v  # u' = v
    dv_dx = -v / x - u  # v' = -v/x - u

    return np.array([du_dx, dv_dx])


def control_case_3(t, variables):
    x, y, z = variables

    dx_dt = -2 * x + 5 * z
    dy_dt = np.sin(t - 1) * x - y + 3 * z
    dz_dt = -x + 2 * z

    return np.array([dx_dt, dy_dt, dz_dt])
