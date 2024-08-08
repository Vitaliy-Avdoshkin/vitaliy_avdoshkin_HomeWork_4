import pytest
from src.main import *

@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

product1 = 1
product2 = 2
product3 = 3

@pytest.fixture()
def category1():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",[product1, product2, product3])
