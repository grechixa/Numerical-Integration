import numpy as np


def f(x):
    return np.sqrt(2 * x + 1.6) / (1.8 + np.sqrt(0.3 * x**2 + 2.3))


def g(x, y):
    return (x**2 + y) / (1 + x + y**2)


def equasion1(x, y):
    return y * (1 - x)
