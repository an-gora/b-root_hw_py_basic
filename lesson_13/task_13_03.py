class Product:
    def __init__(self, type_of_product: str, name: str, price: int):
        self.type_of_product = type_of_product
        self.name = name
        self.price = price

    def __str__(self):
        return f'type of product - {self.type_of_product}, name - {self.name}, original price - {self.price}'

class ProductStore:
    def __init__(self, name_of_store):
        self.name_of_store = name_of_store
        self.all_products = {}

    def add(self, product, amount):
        store_price = product.price * 1.3
        self.all_products[product] = (store_price, amount)

    # def set_discount(self, identifier, percent, identifier_type=’name’):
    # def sell_product(self, product_name, amount):
    # def get_income(self):
    def get_all_products(self):
        for k,v in self.all_products.items():
            print (k, v)
        # return self.all_products
    # def get_product_info(self, product_name):

p = Product('Sport', 'Football T-Shirt', 100)
s = ProductStore('new store')
s.add(p, 10)
s.get_all_products()
