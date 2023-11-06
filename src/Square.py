from src.Figure import Figure


class Square(Figure):
    """ Базовый класс Квадрата """

    _type = 'Квадрат'
    _side_amount = [1]

    def __init__(self, name, *sides):
        super().__init__(name, self._type, self._side_amount, *sides)
        self.perimetr = self.get_perimetr()
        self.is_valid()

    def is_valid(self):
        if len(set(self.get_sides())) > 1:
            raise ValueError(f'{self}: У {self._type} все стороны должны быть одинаковы\n'
                             f'{self.get_sides()}')

        self.get_area()

    def get_perimetr(self):
        self.perimetr = self.get_side(0) * 4
        return self.perimetr

    def get_area(self):
        self.area = self.get_side(0) * self.get_side(0)
        return self.area
