def f1(x):
    return x**3 - 12 * x - 8


def f2(x):
    return x**3 + 4 * x - 6


def diff(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def second_diff(f, x, h=1e-6):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)


def tangent_method(f, a, b):
    x0 = a

    while True:
        x1 = x0 - (f(x0) / diff(f, x0))
        if abs(x1 - x0) <= 10**-6:
            return x1
        x0 = x1


def bisec_method(f, a, b):
    if f(a) * f(b) > 0:
        return None

    while True:

        x = (a + b) / 2

        if f(a) * f(x) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x
        elif f(x) == 0:
            return x
        else:
            return None

        if abs(a - b) <= 10**-6:
            return x


def chord_method(f, a, b):

    if f(a) * f(b) > 0:
        return None

    f_diff = diff(f, a)
    f_second_diff = second_diff(f, a)

    if f_diff * f_second_diff > 0:
        x0 = a
        C = b
    elif f_diff * f_second_diff < 0:
        x0 = b
        C = a

    while abs(f(x0)) > 1e-6:

        x0 = x0 - (f(x0) / (f(C) - f(x0))) * (C - x0)

    return x0
