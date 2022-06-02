"""
Ввычислить число пи, (использовать Ряд Нилаканта или любой другой вариант расчета числа Пи
c заданной точностью d
"""


def madhava(n):
    from math import exp, log
    s1 = z = 1
    for i in range(1, n + 1):
        s1 = s1 - z / ((2 * i + 1) * exp(i * log(3)))
        z = -z
    s1 = s1 * 12 ** 0.5
    return s1


def nikalant(n):
    s1, z, i = 3, 1, 2
    while i <= n:
        s1 = s1 + 4 * z / (i * (i + 1) * (i + 2))
        i = i + 2
        z = -z
    return s1


def eiler(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / i ** 2
    s = (6 * s) ** 0.5
    return s


from math import pi

d = 200  # Точность заданная
print(f'{pi=}')
print(madhava(d))
print(nikalant(d))
print(eiler(d))
