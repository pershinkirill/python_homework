# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д. Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

in_list = list(input("Please enter the list of numbers with space - ").split(" "))
rev_list = in_list[::-1]
result = []

if (len(in_list) % 2) == 0:
    for i in range(len(in_list) // 2):
        result.append(int(in_list[i]) * int(rev_list[i]))
else:
    for i in range(len(in_list) // 2 + 1):
        result.append(int(in_list[i]) * int(rev_list[i]))

print(result)

