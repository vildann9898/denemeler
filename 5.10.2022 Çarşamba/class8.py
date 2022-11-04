class Pet():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def make_noise(self):
        print(f"I'm {self.name}")

class Fish(Pet):
    def __init__(self, name, age, color, ability):
        super().__init__(name, age, color)
        self.ability = ability

    def make_noise(self):
        pass

class Bird(Pet):
    def __init__(self, name, age, color, size):
        super().__init__(name, age, color)
        self.size = size
    def make_noise(self):
        print("cik cik")
    
nemo = Fish("Nemo",4,"Orange","being lost")
mavis = Bird("Maviş",2,"Blue","medium")
mavis.make_noise()
nemo.make_noise()
        

