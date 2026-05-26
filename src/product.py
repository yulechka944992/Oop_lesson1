class Product:
    """Класс для представления товара: название, описание, цена, количество."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация товара"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# product_1 = Product("огурец", "овощи", 210.0, 3)
# product_2 = Product("помидор", "овощи", 315.50, 5)
# product_3 = Product("лук","овощи",45.0, 8)
# product_4 = Product("банан","фрукты", 120.0, 2)
