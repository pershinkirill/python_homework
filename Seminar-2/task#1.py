# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 0,56 -> 11

number = input("Enter a number: ").replace('.', '')
total = 0

for i in range(len(number)):
    total += int(number[i])

print(total)
