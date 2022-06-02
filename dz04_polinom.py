"""
Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени пример записи в файл
при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0
"""

from random import randint

# n = 10
def make_polinom(n):
    koeff = []
    max_k = 5
    for deg in range(n):
        k = randint(0, max_k)
        koeff.append(k)
    koeff.append(randint(1, max_k))
    polinom = []
    for deg in reversed(range(n + 1)):
        if koeff[deg] != 0:
            element = str(koeff[deg]) if koeff[deg] != 1 or deg == 0 else ''
            if deg > 0:
                element += '*' if koeff[deg] != 1 else ''
                element += 'x'
            if deg > 1:
                element += '^' + str(deg)
            polinom.append(element)

    return ' + '.join(polinom) + ' = 0'


n = int(input("Задайте степень n: "))
polinom_str = make_polinom(n)
print(polinom_str)
file_name = 'polinom.txt'
with open(file_name, 'w') as f:
    print(polinom_str, file=f)