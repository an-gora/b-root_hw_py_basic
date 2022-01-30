class Product:
    def __init__(self, type_of_product: str, name: str, price: int):
        self.type_of_product = type_of_product
        self.name = name
        self.price = price

    def __repr__(self):
        return f'type of product - {self.type_of_product}, name - {self.name}, original price - {self.price}'


class ProductStore:
    def __init__(self):
        self.all_products = {}

    def add(self, product, amount):
        store_price = product.price * 1.3
        self.all_products[product.name] = (product.type_of_product, product.price, store_price, amount)
        print(f'{product.name} in amount of {amount} was added')

    # def set_discount(self, identifier, percent, identifier_type=’name’):
    # def sell_product(self, product_name, amount_to_sell):
    #     for k, v in self.all_products.items():
    #         if k == product_name:
    #             v(amount) = v(amount)-amount_to_sell  # # def get_income(self):
    def get_all_products(self):
        for k, v in self.all_products.items():
            return f'{k}. In this shop price and amount {v}'

    def get_product_info(self, product_name):
        for k,v in self.all_products.items():
            if k == product_name:
              return k, v


p = Product('Sport', 'Football T-Shirt', 100)
s = ProductStore()
s.add(p, 10)
print(s.get_all_products())
print(s.get_product_info('Football T-Shirt'))
