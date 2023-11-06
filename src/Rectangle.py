from src.Figure import Figure


class Rectangle(Figure):
    """ Базовый класс Прямоугольника """

    _type = 'Прямоугольник'
    _side_amount = [2, 4]

    def __init__(self, name, *sides):
        super().__init__(name, self._type, self._side_amount, *sides)
        self.perimetr = self.get_perimetr()
        self.is_valid()

    def is_valid(self):
        if len(set(self.get_sides())) == 1:
            raise ValueError(f'{self}: Такой {self._type} не возможен.\n'
                             f'т.к. содержит все 4 одинаковых стороны: {set(self.get_sides())}\n'
                             f'и не попадает в разрешенное кол-во сторон: {self._side_amount}')

        if len(set(self.get_sides())) not in self._side_amount:
            raise ValueError(f'{self}: Такой {self._type} не возможен.\n'
                             f'т.к. содержит разные стороны: {set(self.get_sides())}\n'
                             f'и не попадает в разрешенное кол-во сторон: {self._side_amount}')

        self.get_area()

    def get_perimetr(self):
        self.perimetr = sum(self.get_sides()[:2]) * 2
        return self.perimetr

    def get_area(self):
        self.area = self.get_side(0) * self.get_side(1)
        return self.area

