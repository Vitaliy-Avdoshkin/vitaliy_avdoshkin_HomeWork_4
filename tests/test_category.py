def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.product_list) == 3


def test_category1_products_property(first_category):
    assert first_category.products == (
        "Название продукта: Samsung Galaxy S23 Ultra, стоимость продукта: 180000.0 руб., количество: 5 шт.\n"
        "Название продукта: Iphone 15, стоимость продукта: 210000.0 руб., количество: 8 шт.\n"
        "Название продукта: Xiaomi Redmi Note 11, стоимость продукта: 31000.0 руб., количество: 14 шт.\n"
    )


def test_category1_add_product(first_category, new_product):
    assert len(first_category.product_list) == 3
    first_category.add_product(new_product)
    assert len(first_category.product_list) == 4
