from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс, является родительским для класса продуктов."""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict, products=None):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass
