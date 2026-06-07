from src.category import Category
from src.product import Product

class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = -1


    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index + 1 < len(self.category.products):
            self.index += 1
            return self.category.products[self.index]
        else:
            raise StopIteration

