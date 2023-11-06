import pytest

from src.Circle import Circle


@pytest.mark.parametrize(('name', 'sides', 'perimetr', 'area'), [
    ('circule1', [1], 6.283185307179586, 3.141592653589793),
    ('circule2', [2], 12.566370614359172, 12.566370614359172)
])
def test_circle_creation(name, sides, perimetr, area):
    cr = Circle(name, *sides)
    assert cr.name == name
    assert cr.area == area
    assert cr.perimetr == perimetr


@pytest.mark.parametrize(('name', 'sides'), [
    ('circule1', [1, 2]),
    ('circule1', [-1]),
    ('circule1', [0]),
    ('circule1', ['asd', 123]),
    ('circule1', ['asd']),
    ('circule1', [123, 'asd']),
])
def test_circle_creation_negative(name, sides):
    with pytest.raises(ValueError):
        cr = Circle(name, *sides)


@pytest.mark.parametrize(('name1', 'sides1', 'name2', 'sides2', 'sum_area'), [
    ('circule1', [1], 'circule2', [2], 15.707963267948966),
])
def test_circle_sums_areas(name1, sides1, name2, sides2, sum_area):
    cr = Circle(name1, *sides1)
    cr2 = Circle(name2, *sides2)
    assert cr.add_area(cr2) == sum_area

@pytest.mark.parametrize(('name1', 'sides1'), [
    ('circule1', [1]),
])
def test_circle_sums_areas_negative(name1, sides1):
    cr = Circle(name1, *sides1)
    with pytest.raises(ValueError):
        cr.add_area(2)


@pytest.mark.parametrize(('name', 'sides', 'perimetr', 'area', 'new_perimetr', 'new_area'), [
    ('circule1', [1], 6.283185307179586, 3.141592653589793, 12.566370614359172, 12.566370614359172),
])
def test_circle_swap_value(name, sides, perimetr, area, new_perimetr, new_area):
    cr = Circle(name, *sides)
    assert cr.name == name
    assert cr.area == area
    assert cr.perimetr == perimetr
    assert cr.get_sides() == [1]

    cr.set_side(0, 2)
    assert cr.area == new_area
    assert cr.perimetr == new_perimetr


@pytest.mark.parametrize(('name', 'sides', 'perimetr', 'area'), [
    ('circule1', [1], 6.283185307179586, 3.141592653589793),
])
def test_circle_swap_value_negative(name, sides, perimetr, area):
    cr = Circle(name, *sides)
    assert cr.name == name
    assert cr.area == area
    assert cr.perimetr == perimetr
    assert cr.get_sides() == sides

    # устанавливаем сторону, индекса которой нет у круга
    cr.set_side(1, 2)
    assert cr.get_sides() == sides

