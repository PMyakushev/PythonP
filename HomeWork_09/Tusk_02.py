'''Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)'''


class TypedMeta(type):
    '''Метакласс, создабщий список __slots__,
    Который будет содержать только атрибуты типа TypedProperty'''
    a = None

    def __call__(self):
        if self.a == None:
            self.a = super().__call__()
        return self.a


class MyClass(metaclass=TypedMeta):
    '''Прикладной пользовательский класс'''

    def method_1(self):
        pass

    def method_2(self):
        print("Небольшоая проблема")


# сингтон
obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
