# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a, b = int(input("Please enter a decimal number, that must be transformed into a binary: ")), ""

while a > 0:
    b = str(a % 2) + b
    a //= 2

print(b)
