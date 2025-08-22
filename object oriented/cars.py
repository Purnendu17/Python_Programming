class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_details(self):
        return("Car Details:",{self.year},{self.brand},{self.model})

car = Car("Porsche", "911 Turbo S", 2023)
print(car.car_details())