# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Enter K number: "))
total = 0

for i in range(1, k + 1):
    print(f"{i} : {round((1 + 1/i)**i, 2)}", end=" ")
    total += (1 + 1 / i) ** i

print(end="\n")

print(f"Sum of the values - {round(total, 2)}")
