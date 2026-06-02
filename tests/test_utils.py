import json
import os
import pytest
import tempfile

from src.category import Category
from src.product import Product
from src.utils import read_json, create_objects_from_json


class TestReadJson:
    """Тесты для функции read_json"""

    def test_read_json_success(self):
        """Тест успешного чтения JSON файла"""
        test_data = [{"name": "Test", "value": 123}]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp_file:
            json.dump(test_data, tmp_file)
            tmp_file_path = tmp_file.name

        try:
            result = read_json(tmp_file_path)
            assert result == test_data
        finally:
            os.unlink(tmp_file_path)

    def test_read_json_file_not_found(self):
        """Тест на отсутствие файла"""
        with pytest.raises(FileNotFoundError):
            read_json("non_existent_file_12345.json")


class TestCreateObjectsFromJson:
    """Тесты для функции create_objects_from_json"""

    def test_create_objects_success(self, sample_json_data):
        """Тест успешного создания объектов из JSON"""
        categories = create_objects_from_json(sample_json_data)

        # Проверяем количество категорий
        assert len(categories) == 2

        # Проверяем типы
        assert isinstance(categories[0], Category)

        products_list = categories[0]._Category__products
        assert isinstance(products_list[0], Product)

        # Проверяем первую категорию
        assert categories[0].name == "Электроника"
        assert categories[0].description == "Различные электронные устройства"
        assert len(products_list) == 2

        # Проверяем продукты в первой категории
        assert products_list[0].name == "Ноутбук"
        assert products_list[0].description == "Мощный игровой ноутбук"
        assert products_list[0].price == 75000.99
        assert products_list[0].quantity == 10

        assert products_list[1].name == "Мышь"
        assert products_list[1].description == "Беспроводная мышь"
        assert products_list[1].price == 1500.50
        assert products_list[1].quantity == 50

        # Проверяем вторую категорию
        assert isinstance(categories[1], Category)
        assert categories[1].name == "Книги"
        assert categories[1].description == "Художественная литература"

        products_list2 = categories[1]._Category__products
        assert len(products_list2) == 1
        assert products_list2[0].name == "Война и мир"
        assert products_list2[0].description == "Роман-эпопея Льва Толстого"
        assert products_list2[0].price == 1200.00
        assert products_list2[0].quantity == 5


class TestIntegration:
    """Интеграционные тесты"""

    def test_read_and_create_objects(self, sample_json_file):
        """Тест чтения JSON файла и создания объектов"""
        data = read_json(sample_json_file)
        categories = create_objects_from_json(data)

        assert len(categories) == 2
        assert isinstance(categories[0], Category)

        products_list = categories[0]._Category__products
        assert isinstance(products_list[0], Product)
        assert categories[0].name == "Электроника"
        assert categories[1].name == "Книги"
        assert products_list[0].price == 75000.99
