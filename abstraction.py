from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("walk")
class Snake(Animal):
    def move(self):
        print("glide")
R=Human()
R.move()
R=Snake()
R.move() 