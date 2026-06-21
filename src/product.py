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
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление товара для пользователя"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод для получения суммы всех товаров на складе"""
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_dict, products=None):
        """Создаёт новый продукт из словаря"""
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]

        if products is not None:
            for product in products:
                if product.name.lower() == name.lower():
                    total_quantity = product.quantity + quantity
                    max_price = max(product.price, price)
                    product.quantity = total_quantity
                    product.price = max_price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer_user = input(f"Цена понижается с {self.__price} до {new_price}. Подтвердите действие (y/n): ")
            if answer_user.lower() == "y":
                self.__price = new_price
                print("Цена изменена")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = new_price


# product_1 = Product("огурец", "овощи", 210.0, 3)
# product_2 = Product("помидор", "овощи", 315.50, 5)
# product_3 = Product("лук","овощи",45.0, 8)
# product_4 = Product("банан","фрукты", 120.0, 2)
