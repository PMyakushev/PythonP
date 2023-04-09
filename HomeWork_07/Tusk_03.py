"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    """Класс работник"""

    def __int__(self, name=str, surname=str, position=str, wage=float, bonus=float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Класс позиции"""

    def get_full_name(self, reverse=False):
        """ Собирает полное имя для позиции в порядке 'заданном reverse
        :param reverse: порядок следования если False (по умолчанию) 'name surname'
         если True, то 'surname name'
        :return: Полное имя
        """
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        """ Вычисляет полный доход (оклад + премия)
        :return: Сумма оклада и премии
        """
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'position': 'Scrum master',
            'wage': 40000,
            'bonus': 0
        },
        {
            'name': 'Petr',
            'surname': 'Petrov',
            'position': 'developer',
            'wage': 90000,
            'bonus': 60000
        },
        {
            'name': 'Irina',
            'surname': 'Ivanova',
            'position': 'service delivery manager',
            'wage': 60000,
            'bonus': 30000
        },
    ]

