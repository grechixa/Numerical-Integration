import numpy as np
from functions import z

def function(x,y):
    return y*(1-x)

import numpy as np

import numpy as np

def Euler(function, a, b, x0, y0, n=10):
    """
    Метод Эйлера для решения ДУ первого порядка y' = f(x, y)
    
    Параметры:
        function: функция f(x, y), возвращающая значение производной
        a, b: границы интервала [a, b]
        x0, y0: начальные условия (обычно x0 == a, y0 == y(a))
        n: количество шагов
    
    Возвращает:
        x: список значений x_i
        y: список значений y_i
    """
    h = (b - a) / n
    x = [x0]
    y = [y0]

    for i in range(n):
        xi = x[i]
        yi = y[i]
        
        # Вычисляем следующее значение по методу Эйлера
        next_y = yi + h * function(xi, yi)
        next_x = xi + h
        
        x.append(next_x)
        y.append(next_y)

    return x, y

# print("=== ПРИМЕР ИСПОЛЬЗОВАНИЯ "Метод Эйлера" ===")
#x_vals,y_vals = Euler(z, 0, 1, 0, 1, 10)
#for i in range(len(x_vals)):
    #print(x_vals, y_vals)

def runge_kutta4(function, a, b, x0, y0, n, x_end):
    h = (b - a) / h

    x = x[0]
    y = y[0]

    for i in range(x_end + 1):
        xi = x[i]
        yi = y[i]

        k1 = h * function(xi,yi)
        k2 = h * function(xi + h / 2, yi + k1 / 2)
        k3 = h * function(xi + h / 2, yi + k2 / 2)
        k4 = h * function(xi + h, yi + k3)

        F = (k1 + 2*k2 + 2*k3 + k4) / 6
        
        x.append(xi)
        y.append(yi)

    return x,y

print(" === ПРИМЕР ИСПОЛЬЗОВАНИЯ Рунге-Кутта 4 порядка === ")
a = 0
b = 1
x_start = 0
y_start = 1
step = 10
max_x = 100

x_vals1, y_vals1 = runge_kutta4(z, a, b, x_start, y_start, step, max_x)

for i in range(len(x_vals1)):
    print(x_vals1, y_vals1)