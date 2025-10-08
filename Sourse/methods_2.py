
# ПЕРЕМЕННЫЙ ШАГ

from func import f
import numpy as np

#E - точность
def alg1(a, b, n, E):
    h = (b - a) / n # шаг 
    IN = 0  # значение интеграла при n разбиений
    R = float('inf')  # начальная погрешность
    while R>E:
        S2 = 0
        x = a
        while x<= (b - h):
            S2 += f(x)
            x+=h
        I2N = h*S2
        R = abs(I2N-IN)
        IN = I2N
        h /= 2
    return I2N
