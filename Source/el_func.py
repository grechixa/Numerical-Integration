from numpy import pi
from math import sin, exp


def exp_row(x):
    s = 1.0
    u = 1.0
    k = 1

    while True:
        u *= x / k
        if abs(u) <= 1e-6:
            break
        s += u
        k += 1

    return s, k


def sin_row(x):
    s = x
    u = x
    k = 1

    while True:
        if k == 0:
            s += u
        else:
            u *= -(x * x) / ((2 * k) * (2 * k + 1))
            if abs(u) <= 1e-6:
                break
            s += u
        k += 1

    return s, k


def exp_Cheb(x):
    s = 0
    a = [0.9999998, 1, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
    for k in range(len(a)):
        s += a[k] * x**k
    return s


def sin_Cheb(x):
    s = 0
    a = [1.000000002, -0.166666589, 0.008333075, -0.000198107, 0.000002608]
    for k in range(len(a)):
        s += a[k] * (x ** (2 * k + 1))
    return s


def sqrt_iter(x, y0=None):

    if y0 == None:
        m = 0
        while True:
            if 2**m > x:
                break
            m += 1

        y0 = 2 ** (m // 2)

    count = 0

    while True:
        y = 1 / 2 * (y0 + x / y0)
        count += 1
        if abs(y - y0) <= 1e-5:
            break
        y0 = y

    return y, count


def reverse_sqrt_iter(x, y0=None):

    if y0 == None:
        m = 0
        while True:
            if 2**m > x:
                break
            m += 1

        y0 = 2 ** (-1 * (m // 2))

    count = 0

    while True:
        y = ((3 / 2) * y0) - ((1 / 2) * x * y0**3)
        count += 1
        if abs(y - y0) <= 1e-5:
            break
        y0 = y

    return y, count
