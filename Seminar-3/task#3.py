# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

minn = int(input("Please enter the minimum value for the list: "))
maxx = int(input("Please enter the maximum value for the list: "))


def rand_list(minimum, maximum):
    random_float_list = []
    for i in range(0, 10):
        x = round(random.uniform(minimum, maximum), 2)
        random_float_list.append(x)
    return random_float_list


lst = rand_list(minn, maxx)
print(f"The randomly generated list - {lst}")
print(f"The minimum element - {min(lst)}, the maximum element - {max(lst)}, difference  "
      f"between min and max - {round(max(lst) - min(lst), 2)}")
