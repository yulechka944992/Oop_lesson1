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

    def __str__(self):
        """Строковое представление категории"""
        count_product = 0
        for product in self.__products:
            count_product += product.quantity
        return f"{self.name}, количество продуктов: {count_product} шт."

    def add_product(self, product: Product):
        """Добавление продукта в список, проверка на возможность добавить другой объект вместо продукта"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Форматированный вывод для пользователя"""
        product_list = []
        for product in self.__products:
            product_str = str(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
            product_list.append(product_str)
        return "\n".join(product_list)

    def get_products_list(self):
        """Доступ к исходному списку продуктов для итерации"""
        return self.__products

    # @property
    # def products(self):
    #     return "".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products)
