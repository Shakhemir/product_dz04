"""
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
"""
lst = [1, 2, 3, 5, 1, 5, 3, 10]
lst2 = list(set(lst))
print(lst2)