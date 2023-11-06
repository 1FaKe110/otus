from src.Figure import Figure
from math import sqrt


class Tryangle(Figure):
    """ Базовый класс Треугольника """

    _type = 'Треугольник'
    _side_amount = [3]

    def __init__(self, name, *sides):
        super().__init__(name, self._type, self._side_amount, *sides)
        self.get_perimetr()
        self.is_valid()

    def is_valid(self):
        result = all(map(lambda x: (self.perimetr / 2 - x) > 0, self.get_sides()))
        if not result:
            raise ValueError(f'{self}: Такой {self._type} не возможен')

        self.get_area()

    def get_perimetr(self):
        self.perimetr = float(sum(self.get_sides()))
        return self.perimetr

    def get_area(self):
        half_perimetr = self.perimetr / 2
        a, b, c = self.get_sides()
        self.area = sqrt(half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))
        return self.area
