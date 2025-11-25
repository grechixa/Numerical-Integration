from numpy import pi


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
        u *= -(x * x) / (2 * k * (2 * k + 1))
        if abs(u) <= 1e-6:
            break
        s += u
        k += 1

    return s, k


print(exp_row(0.5))
print(sin_row(pi / 6))
