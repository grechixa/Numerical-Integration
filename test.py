from scipy.integrate import solve_ivp
import numpy as np


def equasion1(x, y):
    return y * (1 - x)


# Решаем от x=0 до x=1 с начальным условием y(0)=1
solution = solve_ivp(equasion1, (0, 1), [1], t_eval=[1])

print(f"Решение при x=1: y(1) = {solution.y[0][0]:.6f}")
