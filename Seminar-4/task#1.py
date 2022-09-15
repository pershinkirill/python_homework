# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = int(input('Please enter a number: '))
d = input('Please enter the number for accuracy selection : ')

if float(d) < 1:
    count = 0
    while float(d) < 1:
        d = float(d) * 10
        count += 1
    d = count

print(f'{a:.{d}f}')
