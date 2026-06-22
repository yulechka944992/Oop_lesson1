import pytest
import json
import tempfile
import os

from src.product import Product
from src.category import Category
from src.iterator import CategoryIterator
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def first_product():
    """Фикстура с первым продуктом"""
    return Product(
        name="Test Product 1",
        description="Test Description 1",
        price=10,
        quantity=5,
    )


@pytest.fixture
def second_product():
    """Фикстура со вторым продуктом"""
    return Product(
        name="Test Product 2",
        description="Test Description 2",
        price=20,
        quantity=1,
    )


@pytest.fixture
def empty_category():
    """Фикстура с пустой категорией"""
    return Category(name="Test Empty Category", description="Test Description", products=[])


@pytest.fixture
def category_with_products(first_product, second_product):
    """Фикстура с категорией, содержащей продукты"""
    return Category(name="Test Category 1", description="Test Category 1", products=[first_product, second_product])


@pytest.fixture
def categories(empty_category, category_with_products):
    """Фикстура с несколькими категориями для проверки счетчиков"""
    Category.category_count = 0
    Category.product_count = 0

    cat1 = category_with_products
    cat2 = empty_category

    return [cat1, cat2]


@pytest.fixture
def sample_json_data():
    """Тестовые JSON данные"""
    return [
        {
            "name": "Электроника",
            "description": "Различные электронные устройства",
            "products": [
                {"name": "Ноутбук", "description": "Мощный игровой ноутбук", "price": 75000.99, "quantity": 10},
                {"name": "Мышь", "description": "Беспроводная мышь", "price": 1500.50, "quantity": 50},
            ],
        },
        {
            "name": "Книги",
            "description": "Художественная литература",
            "products": [
                {"name": "Война и мир", "description": "Роман-эпопея Льва Толстого", "price": 1200.00, "quantity": 5}
            ],
        },
    ]


@pytest.fixture
def sample_json_file(sample_json_data):
    """Временный JSON файл с тестовыми данными"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="UTF-8") as tmp_file:
        json.dump(sample_json_data, tmp_file, ensure_ascii=False)
        tmp_file_path = tmp_file.name

    yield tmp_file_path

    if os.path.exists(tmp_file_path):
        os.unlink(tmp_file_path)


@pytest.fixture
def category_iterator(category_with_products):
    """Фикстура для итератора, использующая другую фикстуру"""
    return CategoryIterator(category_with_products)


@pytest.fixture
def smartphone1():
    return Smartphone("Iphone 17", "512GB, Gray space", 180000, 1, "98.2", "17", 512, "Gray space")


@pytest.fixture
def smartphone2():
    return Smartphone("Honor", "256GB, White", 80000, 1, "92", "50", 256, "White")


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
