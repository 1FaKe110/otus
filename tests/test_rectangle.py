import pytest

from src.Rectangle import Rectangle


@pytest.mark.parametrize(('name', 'sides', 'perimetr', 'area'), [
    ('rct1', [1, 2], 6, 2),
    ('rct2', [2, 2.6], 9.2, 5.2)
])
def test_rectangle_creation(name, sides, perimetr, area):
    rtc = Rectangle(name, *sides)
    assert rtc.name == name
    assert rtc.perimetr == perimetr
    assert rtc.area == area


@pytest.mark.parametrize(('name', 'sides'), [
    ('rct1', [1, 1]),
    ('rct2', ['IFNZTOJP', 1]),
    (None, ['IFNZTOJP', 1]),
    ('rct3', [2, -2])
])
def test_rectangle_creation_negative(name, sides):
    with pytest.raises(ValueError):
        cr = Rectangle(name, *sides)


@pytest.mark.parametrize(('name1', 'sides1', 'name2', 'sides2', 'sum_area'), [
    ('fig1', [1, 2], 'fig2', [2, 2.6], 7.2),
    ('fig1', [2, 1], 'fig2', [2.6, 2], 7.2),
])
def test_sums_areas(name1, sides1, name2, sides2, sum_area):
    rtc1 = Rectangle(name1, *sides1)
    rtc2 = Rectangle(name2, *sides2)

    assert rtc1.add_area(rtc2) == sum_area


@pytest.mark.parametrize(('name', 'sides', 'add_area_value'), [
    ('fig1', [1, 2], '1'),
    ('fig1', [1, 2], 2),
    ('fig1', [1, 2], {2}),
    ('fig1', [1, 2], {2: 3}),
    ('fig1', [1, 2], []),
])
def test_sums_areas_negative(name, sides, add_area_value):
    rtc = Rectangle(name, *sides)
    with pytest.raises(ValueError):
        rtc.add_area(add_area_value)


@pytest.mark.parametrize(
    ('name', 'sides', 'perimetr', 'area', 'new_side_value', 'new_perimetr', 'new_area'), [
        ('fig1', [1, 2], 6, 2, 4, 12, 8)
    ]
)
def test_swap_side(name, sides, perimetr, area, new_side_value, new_perimetr, new_area):
    rtc = Rectangle(name, *sides)
    assert rtc.perimetr == perimetr
    assert rtc.area == area

    rtc.set_side(0, new_side_value)

    assert rtc.perimetr == new_perimetr
    assert rtc.area == new_area
@pytest.mark.parametrize(
    ('name', 'sides', 'new_side_value'), [
        ('fig1', [1, 2], 2)
    ]
)
def test_swap_side_negative(name, sides, new_side_value):
    rtc = Rectangle(name, *sides)
    with pytest.raises(ValueError):
        rtc.set_side(0, new_side_value)

