import pytest

from src import category
from src.product import Product
from src.category import Category
from tests.conftest import first_product, second_product


class TestCategory:
    """Тесты для класса Category"""

    def test_category_empty(self, empty_category):
        """Тест создания пустой категории"""
        assert empty_category.name == "Test Empty Category"
        assert empty_category.description == "Test Description"
        assert empty_category.products == ""

    def test_categories_some(self, category_with_products, first_product, second_product):
        """Тест создания категории с продуктами"""
        assert category_with_products.name == "Test Category 1"
        assert first_product.name in category_with_products.products
        assert second_product.name in category_with_products.products

    def test_category_count_increments(self, categories):
        """Тест увеличения счетчика категорий"""
        Category.category_count = 0
        Category.product_count = 0

        cat1 = Category("Cat1", "Desc1", [])
        cat2 = Category("Cat2", "Desc2", [])

        assert Category.category_count == 2

    def test_category_str(self, category_with_products):
        """Тест сторокового формата категории товаров"""
        assert str(category_with_products) == "Test Category 1, количество продуктов: 6 шт."

    def test_products(self):
        """Тест правильного отображения строки"""
        category = Category(name="Test Category", description="Test Description", products=[])
        category.add_product(Product("Product 1", "desc", 1500, 3))

        assert category.products == "Product 1, 1500 руб. Остаток: 3 шт."

    def test_add_product_error(self):
        """Тест ошибки при добавлении некорректного товара"""
        category = Category("Электроника", "Смартфоны", [])
        with pytest.raises(TypeError):
            category.add_product("не продукт")

        with pytest.raises(TypeError):
            category.add_product(123)

    def test_middle_price(self, category_with_products):
        """Тест успешной работы функции по подсчету средней цены"""
        assert category_with_products.middle_price() == 15

    def test_middle_price_empty_cat(self, empty_category):
        """Тест подсчета средней цены товара из пустой категории"""
        assert empty_category.middle_price() == 0
