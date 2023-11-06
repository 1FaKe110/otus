from __future__ import annotations


class Figure:
    """ Базовый класс фигуры """

    area = None
    perimetr = None

    def __init__(self, name, figure_type, side_amount, *sides):
        self.name = str(name)
        self._type = figure_type
        self.side_amount = side_amount
        self.__check__(*sides)
        self.__sides = sorted(sides)

    def __repr__(self):
        return f'{self._type} [#{self.name :<5}]'

    def __check__(self, *sides):
        if len(sides) not in self.side_amount:
            raise ValueError(f"{self}: Кол-во сторон {self._type}a не соблюдено:\n "
                             f"  - указано: {len(sides)}\n "
                             f"  - разрешено: {self.side_amount}")

        if not all(map(lambda x: isinstance(x, int) or isinstance(x, float), sides)):
            raise ValueError(f"{self}: У одной из сторон не верный тип данных")

        if not all(map(lambda x: x > 0, sides)):
            raise ValueError(f"{self}: Одна из сторон {self._type}a меньше нуля")

    def add_area(self, fig):
        """ sums figures ares """
        if not isinstance(fig, Figure):
            raise ValueError(f"{fig} ({type(fig)}) is not subclass of {Figure}")

        return self.area + fig.area

    def is_valid(self):
        pass

    def get_perimetr(self):
        pass

    def get_area(self):
        pass

    def set_side(self, side_id, value):
        try:
            self.__sides[side_id] = value
        except IndexError:
            print(f"{self}: Попытка записи в несуществующую сторону с id: {side_id}. Данные не были изменены")

        self.get_perimetr()
        self.is_valid()

    def get_side(self, side_id):
        try:
            return self.__sides[side_id]
        except IndexError:
            print(f"{self}: Стороны с id: {side_id} не существует")

    def get_sides(self):
        return self.__sides
