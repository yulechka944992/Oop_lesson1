from src.product import Product


class LawnGrass(Product):
    """Дочерний класс для родительского класса Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Инициализация родительского класса расширяется новыми атрибутами
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
