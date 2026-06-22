import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Iphone 17"
    assert smartphone1.description == "512GB, Gray space"
    assert smartphone1.price == 180000
    assert smartphone1.quantity == 1
    assert smartphone1.efficiency == "98.2"
    assert smartphone1.model == "17"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 260000


def test_smartphone_add_error(smartphone1):
    with pytest.raises(TypeError):
        result = smartphone1 + 1
