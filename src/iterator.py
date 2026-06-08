from src.category import Category
from src.product import Product


class CategoryIterator:
    """Вспомогательный класс для итерации товаров в заданной категории"""

    def __init__(self, category):
        self.category = category
        self.index = -1

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        products_list = self.category.get_products_list()

        if self.index + 1 < len(products_list):
            self.index += 1
            return products_list[self.index]
        else:
            raise StopIteration
