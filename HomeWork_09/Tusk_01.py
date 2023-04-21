# class Descriptor:
#     def __init__(self, atr):
#         self.atr = atr
#
#     # def __get__(self, instance, owner): # instance = обьект класса(Road), owner = класс Road
#     #     return instance.__dict__[self.atr]
#
#     def __set__(self, instance, value):
#         if isinstance(value, int):
#             print(value)
#         else:
#             raise TypeError("Только тип Int")
#         if value < 0:
#             raise ValueError("больше 0")
#         self.atr = value
#
#     # def __delete__(self, instance):
#     #     del instance.__dict__[self.atr]
#
#
# class Road():
#     # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см
#     # Определяю его как private из соображений, что это константа, не подлежащая изменению
#     __weight = 0.5
#
#     length = Descriptor('length')
#     width = Descriptor('width')
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         print(f'Создан новый объект класса Road длиной {self.length} метров и шириной {self.width} метров')
#
#     def get_weight(self, thickness):
#         ret_val = self.length.atr * self.width.atr * thickness * self.__weight
#         print(f'Вес асфальта, требуемый для укладки полотна толщиной {thickness} см, равен {ret_val} т')
#
#         return ret_val
#
#
# r1 = Road(100, 10)
# w1 = r1.get_weight(10)
#
# r2 = Road(1000, 20)
# w2 = r2.get_weight(20)
#
# print(f'Суммарный вес асфальта для двух объектов = {w1 + w2}')



# class NonType:
#     def __set__(self, instance, value):
#         if value < 0:
#             raise NameError("Должнен быть кортеж ")
#         instance.__dict__[self.my_attr] = value
#
# class Matrix:
#
#     '''Реализация класса матрикс'''
#
#     def __init__(self, *args):  # *args кортеж
#         self.new_lst = list(args)
#
#
#     def __add__(self, other):
#         res = []
#         for i in range(len(self.new_lst)):
#             line = []
#             for j in range(len(self.new_lst[i])):
#                 line.append(self.new_lst[i][j] + other.new_lst[i][j])
#             res.append(line)
#         return Matrix(res)
#
#     def __str__(self):
#         return str(self.new_lst[0])
#
#
#
#
# obj_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
# obj_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
# print(obj_1 + obj_2)
