class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"{'Product name':<13}: {self.name}")
        print(f"{'Category':<13}: {self.category}")
        print(f"{'Price':<13}: ${self.price:.2f}")
        print(f"{'Quantity':<13}: {self.quantity}")
        print("--------------------")

    def inventory_value(self):
        total = self.price * self.quantity
        print(f"{'Inventory Value':<13}: ${total:.2f}")
        print("--------------------")

name1 = input("Enter product 1 name: ")
category1 = input("Enter product 1 category: ")
price1 = float(input("Enter product 1 price: "))
quantity1 = int(input("Enter product 1 quantity: "))

name2 = input("Enter product 2 name: ")
category2 = input("Enter product 2 category: ")
price2 = float(input("Enter product 2 price: "))
quantity2 = int(input("Enter product 2 quantity: "))

product1 = Product(name1, category1, price1, quantity1)
product2 = Product(name2, category2, price2, quantity2)

print(f"===== Product 1: {product1.name} =====")
print(f"Product 1: {product1.name}   {product1.category}")
product1.display_info()
product1.inventory_value()

print(f"===== Product 2: {product2.name} =====")
print(f"Product 2: {product2.name}   {product2.category}")
product2.display_info()
product2.inventory_value()