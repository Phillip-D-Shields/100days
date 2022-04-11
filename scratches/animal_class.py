class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.num_legs = 4

    def breathe(self):
        print("Breathing")


class Fish(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.num_legs = 0

    def breathe(self):
        Animal.breathe(self)
        print("Breathing underwater")

    @staticmethod
    def swim():
        print("Swimming")


nemo = Fish()
nemo.breathe()
nemo.swim()
print(f"{nemo.num_legs} legs")