# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = int(input('Please enter a number: '))
d = input('Please enter the number for accuracy selection : ')

# Because accuracy can be input two ways (d = 4 or d = 0.0001) we have to anticipate this situation
if float(d) < 1:
    count = 0
    while float(d) < 1:
        d = float(d) * 10
        count += 1
    d = count

print(f'{a:.{d}f}')
