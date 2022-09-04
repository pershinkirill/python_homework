# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
a, b, c = int(input("enter X: ")), int(input("enter Y: ")), int(input("enter Z: "))

left = not (a or b or c)
right = not a and not b and not c

print(left == right)
