# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#a, b, c = int(input("enter X: ")), int(input("enter Y: ")), int(input("enter Z: "))

for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            left = not (a or b or c)
            right = not a and not b and not c
            print(f"left - {left} | right - {right}")
            print(f"a - {a} | b - {b} | c - {c}")

#The left part of the equation
#left = not (a or b or c)
#The truth table for the left part of the equation
# X	| Y	| Z	| X ⋁ Y ⋁ Z	|¬(X ⋁ Y ⋁ Z)
# 0	| 0	| 0	|     0	    |      1
# 0	| 0	| 1	|     1	    |      0
# 0	| 1	| 0	|     1	    |      0
# 0	| 1	| 1	|     1	    |      0
# 1	| 0	| 0	|     1	    |      0
# 1	| 0	| 1	|     1	    |      0
# 1	| 1	| 0	|     1	    |      0
# 1	| 1	| 1	|     1	    |      0

#The right part of the equation
#right = not a and not b and not c
#The truth table for the right part of the equation
# X	| Y	| Z	|¬X	|¬Y	|¬Z	|¬X ⋀ ¬Y ⋀ ¬Z
# 0	| 0	| 0	| 1	| 1	| 1	|      1
# 0	| 0	| 1	| 1	| 1	| 0	|      0
# 0	| 1	| 0	| 1	| 0	| 1	|      0
# 0	| 1	| 1	| 1	| 0	| 0	|      0
# 1	| 0	| 0	| 0	| 1	| 1	|      0
# 1	| 0	| 1	| 0	| 1	| 0	|      0
# 1	| 1	| 0	| 0	| 0	| 1	|      0
# 1	| 1	| 1	| 0	| 0	| 0	|      0

print(left == right)
