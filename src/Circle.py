from src.Figure import Figure
from math import pi


class Circle(Figure):
    """
    Базовый класс Круга\n
    У круга 1 сторона - его периметр.\n
    Выбрал реализацию, где стороной круга будет считаться радиус
    """

    _type = 'Круг'
    _side_amount = [1]

    def __init__(self, name, *sides):
        super().__init__(name, self._type, self._side_amount, *sides)
        self.get_perimetr()
        self.is_valid()

    def is_valid(self):
        self.get_area()

    def get_perimetr(self):
        self.perimetr = pi * (self.get_side(0) * 2)
        return self.perimetr

    def get_area(self):
        self.area = pi * (self.get_side(0)) ** 2
        return self.area

