class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 50
        self.happiness = 50

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age, roar=8):
        super().__init__(name, age)
        self.roar = roar
        self.health = 60
        self.happiness = 70

class Tiger(Animal):
    def __init__(self, name, age, stealth=6):
        super().__init__(name, age)
        self.stealth = stealth
        self.health = 65
        self.happiness = 55

class Monkey(Animal):
    def __init__(self, name, age, speed=10):
        super().__init__(name, age)
        self.swing = speed
        self.health = 70
        self.happiness = 80

class Bear(Animal):
    def __init__(self, name, age, fur_thickness=12):
        super().__init__(name, age)
        self.fur_thickness = fur_thickness
        self.health = 75
        self.happiness = 60

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_lion(self, name, age):
        self.animals.append(Lion(name, age))

    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))

    def add_monkey(self, name, age):
        self.animals.append(Monkey(name, age))

    def add_bear(self, name, age):
        self.animals.append(Bear(name, age))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()

    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()
        return self

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 3)
zoo1.add_lion("Simba", 5)
zoo1.add_tiger("Rajah", 4)
zoo1.add_tiger("Shere Khan", 7)
zoo1.add_monkey("Nami", 2)
zoo1.add_bear("Lofi", 3)

zoo1.print_all_info()
zoo1.feed_all_animals().print_all_info()