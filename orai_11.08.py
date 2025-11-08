class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
            print(f"A(z) {self.brand} {self.model} beindult.")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = car("Toyota", "Corolla", 2020)
car2 = car("Ford", "Mustang", 2022)

car1.start()
car2.start()

print(car1)
print(car2)

class ElectricCar(car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start(self):
        print(f"A(z) {self.brand} {self.model} hangtalanul indul.")

car1 = car("Ford", "Mustang", 2022)
e_car = ElectricCar("Mercedes", "EQS", 2024, 75)

car1.start()
e_car.start()
