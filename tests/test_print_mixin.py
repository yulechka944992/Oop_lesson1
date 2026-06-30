from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_print_mixin(capsys):
    Product("Продукт №1", "Тестовый продукт", 100, 1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Продукт №1, Тестовый продукт, 100, 1)"

    Smartphone("Iphone 17", "512GB, Gray space", 180000, 1, "98.2", "17", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 17, 512GB, Gray space, 180000, 1)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
