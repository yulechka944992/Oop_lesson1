from src.product import Product


class Smartphone(Product):
    """Дочерний класс от Product"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Импорт конструктора из родительского класса и расширение новыми атрибутами
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color