"""
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
содержащий сумму многочленов. (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)
"""

in_files = "polinom.txt", "polinom2.txt"
out_file = "summ_polinom.txt"


def read_polinom(file):
    with open(file) as f:
        polinom_list = f.readline().strip().split(' = ')[0].split(' + ')
    # print(polinom_list)
    koeff_dict = dict()
    for i in polinom_list:
        if 'x' not in i:
            koeff_dict[0] = int(i)
        else:
            if '^' not in i:
                deg = 1
            else:
                deg = int(i.split('^')[1])
            if '*' not in i:
                koeff_dict[deg] = 1
            else:
                koeff_dict[deg] = int(i.split('*')[0])
    return koeff_dict


def summ_of_polinoms(*koeffs):
    result = dict()
    for polinom in koeffs:
        # print(polinom)
        for deg, koeff in polinom.items():
            # print(deg, koeff, end=';')
            if deg not in result:
                result[deg] = koeff
            else:
                result[deg] += koeff
    # print(result)
    return result

def make_polinom_str(koeffs):
    degs = list(koeffs.keys())
    degs.sort()
    degs.reverse()
    polinom = []
    for deg in degs:
        if koeffs[deg] != 0:
            element = str(koeffs[deg]) if koeffs[deg] != 1 or deg == 0 else ''
            if deg > 0:
                element += '*' if koeffs[deg] != 1 else ''
                element += 'x'
            if deg > 1:
                element += '^' + str(deg)
            polinom.append(element)
    return ' + '.join(polinom) + ' = 0'


polinom1 = read_polinom(in_files[0])
polinom2 = read_polinom(in_files[1])

polinom3 = summ_of_polinoms(polinom1, polinom2)

polinom_str = make_polinom_str(polinom3)
print(polinom_str)
file_name = 'polinom_summ.txt'
with open(file_name, 'w') as f:
    print(polinom_str, file=f)
