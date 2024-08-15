def test_main(product_samsung, product_iphone, product_xiaomi):
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


def test_product_price_setter(capsys, product_iphone):
    product_iphone.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product_iphone.price = 210000.0
    assert product_iphone.price == 210000.0
