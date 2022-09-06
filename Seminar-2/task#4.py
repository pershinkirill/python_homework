# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from numpy.random import randint #importing random integers generator

n = int(input("Entre N number: "))

rand_list = randint(-n, n, n)
print(f"Random list in range from {-n} to {n} {rand_list}")

text = open("file.txt", "r")
text = text.readlines()
total = 1
i = 0

while i < len(text):
    total *= int(rand_list[int(text[i])])
    i += 1

print(total)
