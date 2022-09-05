# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 0,56 -> 11

number = input("Enter a number: ").split(".")

# for float numbers
if len(number) == 2:
    number = number[0] + number[1]
    i = 0
    total = 0
    while i < len(number):
        total += int(number[i])
        i += 1

#in case if the number is not float
else:
    total = 0
    for i in range(len(number[0])):
        total += int(number[0][i])

print(total)
