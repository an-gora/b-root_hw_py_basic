class Product:
    def __init__(self, type_of_product: str, name: str, price: int):
        self.type_of_product = type_of_product
        self.name = name
        self.price = price

    def __repr__(self):
        return f'type of product - {self.type_of_product}, name - {self.name}, original price - {self.price}'


class ProductCard:
    def __init__(self, product, amount):
        self.type_of_product = product.type_of_product
        self.name = product.name
        self.price = product.price
        self.store_price = self.price*1.3
        self.amount = amount

    def __repr__(self):
        return f'type of product - {self.type_of_product}, name - {self.name}, original price - {self.price}, store price - {self.store_price}, amount - {self.amount}'


class ProductStore:
    def __init__(self):
        self.income = None
        self.all_products = {}

    def add(self, product, amount):
        self.all_products[product.name] = ProductCard(product, amount)
        print(f'{product.name} in amount of {amount} was added')

    def set_discount(self, percent, identifier_type='', identifier_name = ''):
        for k, v in self.all_products.items():
            if k == identifier_name or v.type_of_product == identifier_type:
                v.store_price = v.store_price * (1 - percent/100)

    def sell_product(self, product_name, amount_to_sell):
        for k, v in self.all_products.items():
            if k == product_name:
                return v[-1]

    def get_all_products(self):
        for k, v in self.all_products.items():
            return f'{k}. In this shop price {v.store_price} and amount {v.amount}'

    def get_product_info(self, product_name):
        for k, v in self.all_products.items():
            if k == product_name:
                return k, v.amount

    def get_income(self):
        return self.income

    def sell_product(self, product_name, amount):
        for k, v in self.all_products.items():
            if k == product_name:
                    if v.amount >= amount:
                        v.amount = v.amount - amount
                        self.income = amount*v.store_price
                    else:
                        raise Exception('not enough to sell')



p = Product('Sport', 'Football T-Shirt', 100)
# prod_card = ProductCard(p, 10)
# print(prod_card)
s = ProductStore()
s.add(p, 10)
# s.set_discount(10, identifier_name = 'Football T-Shirt')
s.sell_product('Football T-Shirt', 5)
print(s.get_all_products())
print(s.get_income())
# print(s.get_product_info('Football T-Shirt'))
# print(s.sell_product('Football T-Shirt', 5))
# print(s.get_all_products())

