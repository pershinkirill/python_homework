# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("enter a number:"))

if (a > 0) and (a < 6):
    print("No, this is a workday")

elif (a > 5) and (a < 8):
    print("Yes, this is a weekend")

else:
    print("There's no such a day in a week")