from src.iterator import CategoryIterator


def test_iterator_works(category_iterator):
    """Тест нормальной работы итератора"""
    products = list(category_iterator)
    assert len(products) == 2
    assert products[0].name == "Test Product 1"
    assert products[1].name == "Test Product 2"


def test_empty_iterator(empty_category):
    """Тест работы итератора с пустой категорией"""
    iterator = CategoryIterator(empty_category)
    products = list(iterator)
    assert len(products) == 0
    assert products == []
