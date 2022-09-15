# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

eps = 0.0001
s = 0
s1 = 1
x = int(input(' '))
k = 0
while abs(s1 - s)> eps:
    s1 = pow(x, k)/math.factorial(k)
    s += s1
    k += 1
    print(float(x))