import numpy as np

# Численное интегрирование
def f(x):
    return np.sqrt(2*x+1.6)/(1.8+np.sqrt(0.3*x**2+2.3))

def g(x,y):
      return (x**2 + y) / (1 + x + y**2)

# Диффернциальное уравнение
def z(x0=0, y0=1):
    if not isinstance(x0, (int, float)):
        raise TypeError(f"x0 должно быть число, получено {type(x0).__name__}")
    if not isinstance(y0, (int, float)):
        raise TypeError(f"x0 должно быть число, получено {type(y0).__name__}")

    y_pr = y0 * (1 - x0)
    return y_pr