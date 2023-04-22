"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

for s in ['attribute','класс','функция','type']:
    try:
        print(s,type(s),s.encode('ascii'), ' - encoding to bytes successful ')
    except:
        print(s,type(s),' - not valid input for bytes string')