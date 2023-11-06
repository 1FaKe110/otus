import pytest
from src.Square import Square


@pytest.mark.parametrize(('name', 'sides', 'perimetr', 'area'), [
    ('sqr1', [1], 4, 1),
    ('sqr1', [2], 8, 4),
    ('sqr1', [2.4], 9.6, 5.76)
])
def test_creation(name, sides, perimetr, area):
    sqr = Square(name, *sides)
    assert sqr.name == name
    assert sqr.perimetr == perimetr
    assert sqr.area == area


@pytest.mark.parametrize(('name', 'sides'), [
    ('sqr1', [1, 1, 1, 1]),
    ('sqr1', [1, 1, 1]),
    ('sqr1', [1, 1]),
    ('sqr2', ['IFNZTOJP', 1]),
    (None, ['IFNZTOJP', 1]),
    ('sqr3', [2, -2]),
    ('sqr4', [2, 3])
])
def test_creation_negative(name, sides):
    with pytest.raises(ValueError):
        sqr = Square(name, *sides)


@pytest.mark.parametrize(('name1', 'sides1', 'name2', 'sides2', 'sum_area'), [
    ('sqr1', [1], 'sqr2', [2.4], 6.76),
    ('sqr1', [2], 'sqr2', [2], 8)
])
def test_sums_areas(name1, sides1, name2, sides2, sum_area):
    sqr1 = Square(name1, *sides1)
    sqr2 = Square(name2, *sides2)

    assert sqr1.add_area(sqr2) == sum_area


@pytest.mark.parametrize(('name', 'sides', 'add_area_value'), [
    ('sqr1', [2], '1'),
    ('sqr1', [2], 2),
    ('sqr1', [2.5], {2}),
    ('sqr1', [2], {2: 3}),
    ('sqr1', [1], []),
])
def test_sums_areas_negative(name, sides, add_area_value):
    sqr = Square(name, *sides)
    with pytest.raises(ValueError):
        sqr.add_area(add_area_value)


@pytest.mark.parametrize(
    ('name', 'sides', 'perimetr', 'area', 'new_side_value', 'new_perimetr', 'new_area'), [
        ('fig1', [2], 8, 4, 4, 16, 16)
    ]
)
def test_swap_side(name, sides, perimetr, area, new_side_value, new_perimetr, new_area):
    rtc = Square(name, *sides)
    assert rtc.perimetr == perimetr
    assert rtc.area == area

    rtc.set_side(0, new_side_value)

    assert rtc.perimetr == new_perimetr
    assert rtc.area == new_area



@pytest.mark.parametrize(
    ('name', 'sides', 'side_index', 'new_side_value'), [
        ('fig1', [2], 3, 4)
    ]
)
def test_swap_side_negative(name, sides, side_index, new_side_value):
    rtc = Square(name, *sides)
    rtc.set_side(side_index, new_side_value)
    assert rtc.get_sides() == sides

