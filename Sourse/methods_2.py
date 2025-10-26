# ПЕРЕМЕННЫЙ ШАГ

from func import f
import numpy as np

#E - точность
def adaptive_left_rectangles(a, b, n, E):
    h = (b - a) / n # шаг 

    def integral(h):
        x = a
        S = 0
        while x <= (b-h):
            S+=f(x)
            x+=h
        return h*S
    
    IN = integral(h)
    R = float('inf')

    while R > E:
        h/=2
        IN2 = integral(h)
        R = abs(IN2-IN)
        IN = IN2

    return IN2
