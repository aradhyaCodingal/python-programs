class BMW:

    def fuel_type(self):
        print("BMW uses Petrol")

    def speed(self):
        print("BMW speed is 250 km/h")


class Ferrari:

    def fuel_type(self):
        print("Ferrari uses Petrol")

    def speed(self):
        print("Ferrari speed is 340 km/h")


# Polymorphism
for car in (BMW(), Ferrari()):
    car.fuel_type()
    car.speed()
    print()