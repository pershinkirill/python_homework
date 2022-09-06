#Реализуйте алгоритм перемешивания списка.

from numpy.random import randint, shuffle

n = int(input("Entre N number: "))

rand_list = randint(-n, n, n)
print(f"Random list in range from {-n} to {n} {rand_list}")

shuffle(rand_list)
print(f"Shuffled list - {rand_list}")
