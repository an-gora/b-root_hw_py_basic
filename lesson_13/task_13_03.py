class Product:
    def __init__(self, type_of_product, name, price):
        self.type_of_product = type_of_product
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self, name_of_store):
        self.name_of_store = name_of_store
        self_all_products = {}

    def add(self, product, amount):
    def set_discount(self, identifier, percent, identifier_type=’name’):
    def sell_product(self, product_name, amount):
    def get_income(self)
    def get_all_products(self)
    def get_product_info(self, product_name)
