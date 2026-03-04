class vehicle:
    def __init__(self, name , maxspeed,milage):
        self.name=name
        self.maxspeed=maxspeed
        self.milage=milage

class bus(vehicle):
    pass
ob=bus("school volvo",180,30)
print("vehicle name:",ob. name,"maximum speed",ob.maxspeed,"milage",ob.milage)
