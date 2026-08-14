class vehicle:
    vehicle_count = 0

    def __init__(self, brand):
        self.brand = brand
        vehicle.vehicle_count += 1


class car(vehicle):
    vehicle_type = "car"

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class electriccar(car):
    vehicle_type = "electriccar"

    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    @classmethod
    def vehicle_no(cls):
        print("Total vehicles:", cls.vehicle_count)

    @staticmethod
    def battery_check(capacity):
        return capacity > 30

    def display(self):
        print(f"{self.brand}, {self.model}, {self.battery} kWh")


v = vehicle("Honda")

c = car("Toyota", "Camry")

e = electriccar("Tesla", "Model 3", 60)

e.display()

electriccar.vehicle_no()

print(electriccar.battery_check(60))
print(electriccar.battery_check(20))