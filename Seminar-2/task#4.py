# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#importing random integers generator
from numpy.random import randint

n = int(input("Entre N number: "))

#A random list generation
rand_list = randint(-n, n, n)
print(f"Random list in range from {-n} to {n} {rand_list}")

#reading the data from file.txt
text = open("file.txt", "r")
text = text.readlines()
total = 1
i = 0

#going through numbers in the doc, using them as indexes for the previously generated list
while i < len(text):
    total *= int(rand_list[int(text[i])])
    i += 1

print(f"The total product of selected numbers - {total}")
