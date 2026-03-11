class bird:
    def __init__(self):
        print("bird is instantiated")
    def whoIsThis(self):
        print("bird")
    def Run(self):
        print("can swim")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is insanitated")
    def whoIsThis(self):
        print("penguin")
    def swim(self):
        print("cant swim")

ob=penguin()
ob.whoIsThis()
ob.swim()
ob.Run()
