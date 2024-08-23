import pytest
from src.product import Product

def test_product_init(
    product_samsung,
    product_iphone,
    product_xiaomi,
    smartphone1,
    smartphone2,
    smartphone3,
):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5

    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8

    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14

    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"

    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.description == "1024GB, Синий"
    assert smartphone3.price == 31000.0
    assert smartphone3.quantity == 14
    assert smartphone3.efficiency == 90.3
    assert smartphone3.model == "Note 11"
    assert smartphone3.memory == 1024
    assert smartphone3.color == "Синий"


def test_smartphone_init(smartphone1, smartphone2, smartphone3):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"

    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.description == "1024GB, Синий"
    assert smartphone3.price == 31000.0
    assert smartphone3.quantity == 14
    assert smartphone3.efficiency == 90.3
    assert smartphone3.model == "Note 11"
    assert smartphone3.memory == 1024
    assert smartphone3.color == "Синий"


def test_product_price_setter(capsys, product_iphone):
    product_iphone.price = 0
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-1]
        == "Цена не должна быть нулевая или отрицательная"
    )
    product_iphone.price = 210000.0
    assert product_iphone.price == 210000.0


def test_product_str(products):
    assert str(products) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_samsung, product_iphone, product_xiaomi):
    assert product_samsung + product_iphone == 2580000
    assert product_samsung + product_xiaomi == 1334000
    assert product_xiaomi + product_iphone == 2114000


def test_product_add_error(smartphone1, grass1, product_xiaomi):
    with pytest.raises(TypeError):
        assert smartphone1 + grass1


# def test_custom_exception(capsys, product_invalid):
#
#     message = capsys.readouterr()
#     assert message.out.strip() == "Товар с нулевым количеством не может быть добавлен"


def test_custom_exception(capsys):
    Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    message = capsys.readouterr()
    assert message.out.strip() == "Товар с нулевым количеством не может быть добавлен"