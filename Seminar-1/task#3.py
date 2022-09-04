# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34;  y=-30 -> 4
# - x=2;   y=4   -> 1
# - x=-34; y=-30 -> 3

x, y = int(input("Enter X: ")), int(input("Enter Y: "))

if (x > 0) and (y > 0):
    print("The point lies on I - quadrant")
elif (x > 0) and (y < 0):
    print("The point lies on IV - quadrant")
elif (x < 0) and (y > 0):
    print("The point lies on II - quadrant")
elif (x < 0) and (y < 0):
    print("The point lies on III - quadrant")

elif (x == 0) and (y == 0):
    print("This is an origin point")
elif (x == 0) and (y != 0):
    print("This point lies on the x-axis")
elif (x != 0) and (y == 0):
    print("This point lies on the Y-axis")
