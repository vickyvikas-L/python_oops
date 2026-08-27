class Vehicle:
    def vehicle_type(self):
        print("This is a vehicle")


class Car(Vehicle):
    def car_type(self):
        print("This is a car")


class SportsCar(Car):
    def speed(self):
        print("Sports car speed is 250 km/h")


s = SportsCar()

s.vehicle_type()
s.car_type()
s.speed()