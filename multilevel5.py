class product:
    product_count = 0

    def __init__(self, name):
        self.name = name
        product.product_count += 1


class electronics(product):
    product_type = "electronics"

    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand
        
class smartphone(electronics):
    product_type = "smartphone"

    def __init__(self, name, brand, discount):
        super().__init__(name, brand)
        self.discount = discount

    @classmethod
    def product_no(cls):
        print("Total products:", cls.product_count)

    @staticmethod
    def discount_check(discount):
        return 0 <= discount <= 50

    def display(self):
        print(f"{self.name}, {self.brand}, {self.discount}%")


p = product("Laptop")

e = electronics("TV", "Samsung")

s = smartphone("Galaxy S25", "Samsung", 20)

s.display()

smartphone.product_no()

print(smartphone.discount_check(30))
print(smartphone.discount_check(70))