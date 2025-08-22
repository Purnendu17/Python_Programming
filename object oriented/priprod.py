class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount
        return self.price

product = Product("Laptop", 1000)
print("Original Price: $",{product.price})

# Apply a 10% discount
product.apply_discount(10)
print("Price after 10% discount: $",{product.price})
