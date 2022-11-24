# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random # will be used for random coefficients generating
import numpy # will be used for a a polynomial generation

k = int(input("Please enter k number, that will be a degree of a polynomial: "))
coeff = []

# generating random list of numbers that will be the polynomial degrees
for i in range(0, k + 1):
    n = random.randint(-10, 10)
    coeff.append(n)

res = ''
for i in range(len(coeff)):
    if coeff[i] == 0:
        continue
    if len(res) > 0 and coeff[i] > 0:
        res += '+'
    if i > (k - 1):
        res += str(coeff[i])
    elif i == (k - 1):
        res += str(coeff[i]) + '*x'
    else:
        res += str(coeff[i]) + '*x^' + str(k - i)
res += ' = 0'

# using numpy generate a polynomial based on our coefficients
# res = numpy.poly1d(coeff)


# Creating a .txt and saving the polynomial there
with open('task#4.txt', 'w') as f:
    f.writelines(str(res))
    f.close()

print(coeff)
print(res)
