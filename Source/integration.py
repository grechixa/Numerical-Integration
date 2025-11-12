import numpy as np
from Source.functions import f, g

# ПОСТОЯННЫЙ ШАГ

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


# ПЕРЕМЕННЫЙ ШАГ

#Алгоритм №1
def algorithm1(a, b, n, eps=1e-6):

    """
    a,b — пределы интегрирования
    eps — требуемая точность ε
    n   — начальное число разбиений
    """

    h = (b - a) / n
    In = 0.0
    I2n = 0.0
    R = float('inf')  # начальная разность

    while R > eps:
        # вычисляем интеграл I2n методом левых прямоугольников
        S2 = 0.0
        x = a
        while x <= b - h:
            S2 += f(x)
            x += h
        I2n = h * S2

        # разность между текущим и предыдущим приближением
        R = abs(I2n - In)
        In = I2n  # обновляем

        # уменьшаем шаг вдвое
        h /= 2

    return I2n



#Алгоритм №2
def algorithm2(a, b, n=10, eps=1e-6):

    """
    a,b — пределы интегрирования
    eps — требуемая точность ε
    n   — начальное число разбиений
    """

    hv = (b - a) / n  # шаг вычисления
    S1 = sum(f(a + i * hv) for i in range(n))
    I1 = S1 * hv

    while True:
        hv /= 2                 # уменьшаем шаг вычисления
        hs = hv                 # шаг смещения
        hd = hv * 2             # шаг движения — как в описании (равен старому hv)
        
        x = a + hs              # смещение от начала
        S2 = 0.0
        while x < b:
            S2 += f(x)
            x += hd             # двигаемся старым шагом (не hv!)
        
        # Уточняем интеграл, добавляя новые точки между старыми
        I2 = (I1 / 2) + S2 * hv

        if abs(I2 - I1) < eps:
            return I2

        I1 = I2

#Кратный интеграл
def double_integral(a1, b1, a2, b2, nx, ny):

    hx = (b1 - a1) / nx
    hy = (b2 - a2) / ny
    s = 0.0

    for i in range(nx):
        x = a1 + i * hx
        for j in range(ny):
            y = a2 + j * hy
            s += g(x, y)

    return s * hx * hy