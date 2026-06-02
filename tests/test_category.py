import pytest
from src.product import Product
from src.category import Category


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
