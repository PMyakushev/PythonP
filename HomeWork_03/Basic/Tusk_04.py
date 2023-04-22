"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

var_1 = int(input('Введите переменную {var_1}: '))
var_2 = int(input('Введите переменную {var_2}: '))
var_3 = int(input('Введите переменную {var_3}: '))

my_array = [var_1, var_2, var_3]


def my_func(*my_array):
    min = var_1
    if min > var_2:
        min = var_2
        if var_2 > var_3:
            min = var_3
    return (var_1 + var_2 + var_3) - min


print('Без функции sort(): ', my_func())

my_array.sort()
print('Используя функцию sort(): ', my_array[1] + my_array[2])
