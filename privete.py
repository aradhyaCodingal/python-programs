class myclass :
    __privateVar=10
    def __privMeth():
        print("this is a private method")
    def hello (self):
        print("value of private variable is :",myclass.__privateVar)
ob=myclass()
ob.__privMeth()
ob.hello()
