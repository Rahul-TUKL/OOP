# Multiple Inheritance********************************************************************
class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand # DO Not Need to  repeat all this
        self.model = model
        self.year = year
    
    def start(self):
        print("vehicle is starting")
    
    def stop (self):
        print("vehicle is stopping")
        
class Car(vehicle):
    def __init__(self, brand, model, year, number_of_doors ,number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels= number_of_wheels

    def starting(self):
        self.start()
        print("The car has started")
        self.stop()
        
class Bike(vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels= number_of_wheels

class Engine(Car): # Multilevel Inheritance: Not a good Example but just for an idea
    def __init__(self, brand =None, model=None, year=0, number_of_doors=0, number_of_wheels=0):
        super().__init__(brand, model, year, number_of_doors, number_of_wheels)
    def start_E(self):
        self.start()
        print("Engine has started")
        self.stop()
        print("Engine has stopped")

# car =Car("Ford", "Focus", 1998, 5 , 4)
# bike =Bike("BMW", "RT", 2011, 2)
# engine=Engine()
# engine.start_E()

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):# Multilevel Inheritence
    def flee(self):
        print(f"{self.name}! Predator is near! Flee!")

class Predator(Animal):
    def attack(self):
        print(f"{self.name}! attacking on the Prey!")

class Rabbit(Prey):
    def __init__(self, name):
        super().__init__(name)
    pass

class Hawk(Predator):
    def __init__(self, name):
        super().__init__(name)
    pass

class Fish(Prey, Predator): #Multiple Inheritence
    def __init__(self, name):
        super().__init__(name)
    pass

rabbit =Rabbit("Tony")
#3rabbit.take_action()
fish =Fish("Mony")
fish.attack()