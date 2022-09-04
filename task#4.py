# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

a = int(input("Enter a quadrant number: "))

if (a < 1) or (a > 4):
    print("There is no such quadrant")

elif a == 1:
    print("Both X and Y happen to consist of positive values in this quadrant")
elif a == 2:
    print("X has negative values in this quadrant and Y has positive values.")
elif a == 3:
    print("Both X and Y have negative values in this quadrant.")
elif a == 4:
    print("X has positive values and Y has negative values")
