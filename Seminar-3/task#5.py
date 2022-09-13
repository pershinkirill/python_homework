# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# NegaFibonacci sequence - Fn = F(n+2)−F(n+1).
# Fibonacci sequence - Fn = F(n-1)+F(n-2).
num = int(input("Please enter a number: "))


def negafibonacci_seq(n):
    fib_lst = [0, 1]
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        fib_lst.append(c)
    nega_fib = fib_lst[::-1]
    for i in range(len(nega_fib) - 1, -1, -2):
        nega_fib[i] = nega_fib[i] * (-1)
    for i in range(1, len(nega_fib)):
        nega_fib.append(fib_lst[i])
    return nega_fib


print(negafibonacci_seq(num))

