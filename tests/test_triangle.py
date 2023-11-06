import pytest
from src.Tryangle import Tryangle


@pytest.mark.parametrize(('name', 'sides', 'perimetr', 'area'), [
    ('tr1', [3, 4, 5], 12, 6),
    ('tr1', [1, 1, 1], 3, 0.4330127018922193),
    ('tr1', [4, 5, 6], 15, 9.921567416492215),
])
def test_creation(name, sides, perimetr, area):
    tr = Tryangle(name, *sides)
    assert tr.name == name
    assert tr.area == area
    assert tr.perimetr == perimetr


@pytest.mark.parametrize(('name', 'sides'), [
    ('tr', [1, 2, 3]),
    ('tr', [1, 1]),
    ('tr', ['IFNZTOJP', 1, 1]),
    (None, ['IFNZTOJP', 1]),
    ('tr', [2, -2, 2]),
    ('tr', [2])
])
def test_creation_negative(name, sides):
    with pytest.raises(ValueError):
        sqr = Tryangle(name, *sides)


@pytest.mark.parametrize(('name1', 'sides1', 'name2', 'sides2', 'sum_area'), [
    ('tr1', [3, 4, 5], 'tr2', [1, 1, 1], 6.43301270189222),
])
def test_sums_areas(name1, sides1, name2, sides2, sum_area):
    tr1 = Tryangle(name1, *sides1)
    tr2 = Tryangle(name2, *sides2)

    assert tr1.add_area(tr2) == sum_area


@pytest.mark.parametrize(('name', 'sides', 'add_area_value'), [
    ('tr1', [1, 1, 1], '1'),
    ('tr1', [1, 1, 1], 2),
    ('tr1', [1, 1, 1], {2}),
    ('tr1', [1, 1, 1], {2: 3}),
    ('tr1', [1, 1, 1], []),
])
def test_sums_areas_negative(name, sides, add_area_value):
    tr = Tryangle(name, *sides)
    with pytest.raises(ValueError):
        tr.add_area(add_area_value)


@pytest.mark.parametrize(
    ('name', 'sides', 'perimetr', 'area', 'new_side_value', 'new_perimetr', 'new_area'), [
        ('fig1', [1, 1, 1], 3, 0.4330127018922193, 0.5, 2.5, 0.24206145913796356)
    ]
)
def test_swap_side(name, sides, perimetr, area, new_side_value, new_perimetr, new_area):
    tr = Tryangle(name, *sides)
    assert tr.perimetr == perimetr
    assert tr.area == area

    tr.set_side(0, new_side_value)

    assert tr.perimetr == new_perimetr
    assert tr.area == new_area


@pytest.mark.parametrize(
    ('name', 'sides', 'side_index', 'new_side_value'), [
        ('fig1', [1, 1, 1], 3, 4)
    ]
)
def test_swap_side_negative(name, sides, side_index, new_side_value):
    tr = Tryangle(name, *sides)
    tr.set_side(side_index, new_side_value)
    assert tr.get_sides() == sides


@pytest.mark.parametrize(
    ('name', 'sides', 'side_index', 'new_side_value'), [
        ('fig1', [1, 1, 1], 2, 2)
    ]
)
def test_swap_side_negative(name, sides, side_index, new_side_value):
    tr = Tryangle(name, *sides)
    with pytest.raises(ValueError):
        tr.set_side(side_index, new_side_value)
