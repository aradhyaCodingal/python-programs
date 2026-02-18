class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name 
        self.age=age

ob=parrot("blu",10)
ob2=parrot("woo",15)
print(ob.name,"is a bird and is",ob.age,"years old")
print(ob2.name,"is a bird and is",ob2.age,"years old")