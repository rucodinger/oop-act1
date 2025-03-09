from module import search

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity=1):
        if not product.in_shop:
            product.in_shop = True
            product.quantity += quantity
            self.products.append(product)
            print("Добавлен новый товар")
        else:
            product.quantity += quantity
            print("Зарегистрирована новая поставка товаров")

    def sell_product(self, name, quantity):
        products = search(name, self.products)[0]
        if len(products) > 0:
            if products[0].quantity >= quantity:
                products[0].quantity -= quantity
            else: print("На складе недостаточно продуктов")
        else: print("Данный товар отсутствует в магазине")

    def get_stock(self, name):
        products = search(name, self.products)[0]
        if len(products) > 0:
            numberOfProducts = products[0].quantity
            print(f"На складе {numberOfProducts} товаров с данным наименованием")
        else: print("Данный товар отсутствует в магазине")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Общая стоимость всех товаров на складе - {total}₽")

class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.in_shop = False

store = Store()
iphone16pro = Product('iPhone 16 Pro', 999)
store.add_product(iphone16pro, 10)
store.sell_product('iPhone 16 Pro', 5)
store.get_stock('iPhone 16 Pro')
store.get_total_value()
