from methods_1 import *
from methods_2 import *
from func import f


print("Trapezoid: ", trapezoid(0,2,10000))
print("Left: ", left(0,2,10000))
print("Right: ", right(0,2,10000))
print("Simpson: ", simpson(0,2,10000))

print("alg1:", adaptive_left_rectangles(0,2,10000,1e-5))
