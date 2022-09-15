# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = int(input('Please enter a number: '))
d = int(input('Please enter the number for accuracy selection : '))

print(f'{a:.{d}f}')
