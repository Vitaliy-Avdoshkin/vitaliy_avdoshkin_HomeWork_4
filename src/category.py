from src.product import Product


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

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.products_counter()} шт."

    @property
    def product_list(self):
        return self.__products

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def products_counter(self):
        products_counter = 0
        for product in self.__products:
            products_counter += product.quantity
        return products_counter

    def middle_price(self):
        try:
            return round(
                sum([product.price for product in self.__products])
                / len(self.__products),
                2,
            )
        except ZeroDivisionError:
            return 0
