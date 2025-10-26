
# ПОСТОЯННЫЙ ШАГ

import numpy as np
from func import f

# Метод трапеций
def trapezoid(a, b, n):
    h = (b-a)/n
    r = 0
    for i in np.arange(a + h, b - h + h/2, h):
        r += f(i)
    return h*((f(a)+f(b))/2+r)

# Метод левых частей
def left(a, b ,n):
    h = (b-a)/n
    r = 0
    for i in np.arange(a,b-h + h/2,h):
        r += f(i)
    return r*h
    
# Метод правых частей
def right(a, b, n):
    h = (b-a)/n
    r = 0
    for i in np.arange(a+h,b+h/2,h):
        r += f(i)
    return r*h

# Метод Симпсона (метод парабол)
def simpson(a, b, n):
    s1 = 0
    s2 = 0
    h = (b-a)/n
    for i in np.arange(a+h,b-h+h/2,2*h):
        s1 += f(i)
    for i in np.arange(a+2*h,b-2*h+h/2,2*h):
        s2 += f(i)
    return (h/3)*(f(a)+f(b)+s1*4+s2*2)
    