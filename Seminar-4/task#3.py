# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности. [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

lst = input('Please enter a list of numbers: ').split()
res = []
temp = []

for i in range(len(lst)):
    if (lst[i] in lst[i + 1:]) or (lst[i] in temp):
        temp.append(lst[i])
    else:
        res.append(int(lst[i]))

print(res)
