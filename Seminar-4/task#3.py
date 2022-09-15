# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности. [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

lst = [1, 1, 2, 3, 4, 5, 5] #input('Please enter a list of numbers: ').split()
res = []

for i in lst:
    count = 0
    if i in lst:
        print(i)
        count += 1
        print(count)
        if count > 1:
            continue
        else:
            res.append(i)

print(res)
