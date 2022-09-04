# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a = input("Enter the first point coordinates X1 and Y1 with space: ")
b = input("Enter the second point coordinates X2 and Y2 with space: ")

def coordintates(x):
    lis = list(x.split(" "))
    return lis

x = coordintates(a)
y = coordintates(b)

#The formula for the distance, between two points whose coordinates are A (x1,y1); B (x2,y2) is:
#√((x1 - x2)^2 + (y1 - y2)^2)

print("The distance between two points is", round(((int(x[0]) - int(y[0]))**2 + (int(x[1]) - int(y[1]))**2)**0.5, 3))

