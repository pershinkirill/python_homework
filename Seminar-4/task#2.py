# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

n = int(input('Please enter a number: '))
res = [] # A list for saving the result


# The function for the integer numbers collection
def integer(x: int):
    intgr = []
    for i in range(1, n + 1):
        if i == 1:
            continue
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count == 2:
            intgr.append(i)
    return intgr


# The function for multipliers collection
def mltpl(x: list, c: int, rslt: list):
    for i in x:
        if c % int(i) == 0:
            c = c / i
            rslt.append(i)
            mltpl(x, c, rslt)
        else:
            continue
        return rslt


print(integer(n))
print(mltpl(integer(n), n, res))
