import pytest


def test_lawngrass_init(lawngrass1):
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"


def test_lawngrass_add(lawngrass1, lawngrass2):
    assert lawngrass1 + lawngrass2 == 16750


def test_lawngrass_error(lawngrass1):
    with pytest.raises(TypeError):
        result = lawngrass1 + 1
