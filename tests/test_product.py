from unittest.mock import patch

import pytest
from src.product import Product
from tests.conftest import first_product


class TestProduct:
    """ "Тесты для класса Product"""

    def test_product_init(self, first_product):
        """Тест создания продукта"""
        assert first_product.name == "Test Product 1"
        assert first_product.description == "Test Description 1"
        assert first_product.price == 10
        assert first_product.quantity == 5

    def test_product_with_zero_quantity(self):
        """Тест с нулевым количеством"""
        product = Product("Out of stock", "No items", 100, 0)
        assert product.quantity == 0

    def test_product_negative_price_not_set(self, first_product):
        """Тест: отрицательная цена не устанавливается"""
        first_product.price = -100
        assert first_product.price == 10

    def test_product_price_without_confirmation(self, first_product):
        """Тест: повышение цены не требует подтверждения"""
        first_product.price = 15
        assert first_product.price == 15

    @patch("builtins.input", return_value="y")
    def test_product_price_y(self, mock_input, first_product):
        first_product.price = 5
        assert first_product.price == 5

    @patch("builtins.input", return_value="n")
    def test_product_price_n(self, mock_input, first_product):
        first_product.price = 5
        assert first_product.price == 10

    def test_new_product_quantity(self, first_product):
        """Тест: при добавлении дубликата складывается количество"""
        products = [first_product]
        product_dict = {"name": "Test Product 1", "description": "Description", "price": 10, "quantity": 3}
        new = Product.new_product(product_dict, products)

        assert first_product.quantity == 8
        assert new == first_product

    def test_new_product_higher_price(self, first_product):
        """Тест: при дубликате выбирается большая цена"""
        products = [first_product]
        product_dict = {"name": "Test Product 1", "description": "Description", "price": 20, "quantity": 3}
        new = Product.new_product(product_dict, products)

        assert first_product.price == 20

    def test_product_str(self, first_product):
        """Тест представления строкового формата товара"""
        assert str(first_product) == "Test Product 1, 10 руб. Остаток: 5 шт."

    def test_product_add(self, first_product, second_product):
        """Тест подсчета всех товаров на складе"""
        assert (first_product + second_product) == 70

    def test_product_add_error(self, smartphone1, lawngrass2):
        """Тест проверяет, что выбрасывается исключение при сложении разных типов товаров"""
        with pytest.raises(TypeError):
            result = smartphone1 + lawngrass2
