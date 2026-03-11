class computer:
    def __init__(self):
        self.__maxPrice=500

    def sell(self):
        print("selling price :",self.__maxPrice)
    
    def setMaxPrice(self,updatedPrice):
        self.__maxPrice=updatedPrice
ob=computer()
ob.sell()
ob.setMaxPrice(8000)
ob.sell()