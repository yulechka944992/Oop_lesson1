import pytest
from src.product import Product


class TestProduct:
    """"Тесты для класса Product"""

    def test_product_init(self, first_product):
        """Тест создания продукта"""
        assert first_product.name == "Test Product 1"
        assert first_product.description == "Test Description 1"
        assert first_product.price == 10
        assert first_product.quantity == 5

    def test_product_with_zero_price(self):
        """Тест с нулевой ценой"""
        product = Product("Free", "Free product", 0, 10)
        assert product.price == 0

    def test_product_with_zero_quantity(self):
        """Тест с нулевым количеством"""
        product = Product("Out of stock", "No items", 100, 0)
        assert product.quantity == 0