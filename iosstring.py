class IOString():
    def __init__(self):
        self.str1=""

    def getString(self):
        self.str1=input("enter the string")
    def printString(self):
        print("reasult",self.str1.upper())
ob = IOString()
 
ob.getString()
ob.printString() 

