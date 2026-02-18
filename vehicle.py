class vehicle:
    def __init__(self, maxSpeed,mileage):
        self.maxSpeed=maxSpeed
        self.mileage=mileage

ob = vehicle(200, 30)
print("model max speed is ",ob.maxSpeed)
print("model mileage is ",ob.mileage)