import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция чтения json-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция создания объектов класса из json"""
    categories = []
    for category_data in data:
        products = [Product(**product_data) for product_data in category_data["products"]]
        categories.append(Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        ))
    return categories

# if __name__ == "__main__":
#     data = read_json("data/products.json")
#     names_data = create_objects_from_json(data)
#
#     print(names_data[0].name)
#     print(names_data[0].products)
