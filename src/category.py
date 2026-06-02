from src.product import Product


class Category:
    """Класс для представления категории товаров"""

    name: str
    description: str
    products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        """Инициализация категории товаров"""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products)


# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
# print(category1.products)
# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
# category1.add_product(product4)
# print(category1.products)
# print(category1.product_count)
