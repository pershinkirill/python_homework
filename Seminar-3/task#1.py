# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

in_str = list(input("Please enter the list of numbers with space - ").split(" "))
counter = 0

for i in range(1, len(in_str), 2):
    counter += int(in_str[i])

print(f"The summ of non even elements is {counter}")
