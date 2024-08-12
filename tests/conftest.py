import pytest

from src.main import Category, Product


@pytest.fixture()
def product_samsung():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_xiaomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def category1():
    product1 = 1
    product2 = 2
    product3 = 3
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture()
def category1_counter():
    product1 = 1
    product2 = 2
    product3 = 3

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture()
def category2():
    product4 = 4
    product5 = 5
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4, product5],
    )


@pytest.fixture()
def product_category_count():
    return
