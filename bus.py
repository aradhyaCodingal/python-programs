class Vehicle:    
    def __init__(self, capacity):       
         self.capacity = capacity   
         def fare(self):       
             return self.capacity * 100
         class Bus(Vehicle):   
             def total_fare(self):                
                      total = self.fare() + (0.10 * self.fare())       
                      return total 
             seats = int(input("Enter number of seats: "))
             bus = Bus(seats)
             print("Total Bus Fare =", bus.total_fare())