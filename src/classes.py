from typing import Any


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict):
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, cost):
        if cost <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = cost


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> Any:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def product_list(self):
        return self.__products

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"Название продукта: {product.name}, стоимость продукта: {product.price} руб., количество: {product.quantity} шт.\n"
        return product_str
