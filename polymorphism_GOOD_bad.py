# poly = Many or multiple
# morph = forms
# Polymorphism = Ability of an object to have multiple forms

#******************************************Good Example of Polymorphism*************************************************************
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year=year

    def start(self):
        print("vehicle is starting")
    
    def stop (self):
        print("vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors=number_of_doors

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year,number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels=number_of_wheels

class Plane(Vehicle):
    def __init__(self, brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors=number_of_doors
    
    def start(self):
        print("Plane is starting")
    
    def stop (self):
        print("Plane is stopping")

# vehicles = [Car("Ford", "Focus", 1998, 4), Motorcycle("BMW", "RT", 1998,2)] 

# for vehicle in vehicles:
#     if isinstance(vehicle, Vehicle):
#         vehicle.start()
#         print(f"We are in a Vehicle Super Class where the vehicle is from {vehicle.brand}, model is {vehicle.model}, from year {vehicle.year} " 
#               f" we are {type(vehicle).__name__} class")
#         vehicle.stop()

vehicles:list[Vehicle] = [Car("Ford", "Focus", 1998, 4), Motorcycle("BMW", "RT", 1998,2), Plane("Boeing", "A380", "2015", "8")] 
for vehicle in vehicles:
    vehicle.start()
    print(f"We are in a Vehicle Super Class where the vehicle is from {vehicle.brand}, model is {vehicle.model}, from year {vehicle.year} " 
            f" we are in a {type(vehicle).__name__} class")
    vehicle.stop()

#************************************************BAD EXample***********************************************************************************
# class car:
#     def __init__(self, brand, model, year, number_of_doors):
#         self.brand = brand
#         self.model = model
#         self.year=year
#         self.number_of_doors = number_of_doors

#     def start(self):
#         print("Here is the car starting")

#     def stop(self):
#         print("Here is the car stopping")

# class Motorcycle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year=year

#     def start(self):
#         print("Here is the Motorcycle starting")

#     def stop(self):
#         print("Here is the Motorcycle stopping")

# vehicles = [car("Ford", "Focus", 1998, 4), Motorcycle("BMW", "RT", 1998)]

# for vehicle in vehicles:
#     if isinstance(vehicle, car):
#         print(f"We are in a Car Class where the car is from {vehicle.brand}, model is {vehicle.model}, from year {vehicle.year} " 
#               f"and with {vehicle.number_of_doors} doors...we are {type(vehicle).__name__} class")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#         print(f"We are in a Car Class where the car is from {vehicle.brand}, model is {vehicle.model}, from year {vehicle.year} " 
#             f"....we are in a {type(vehicle).__name__} class")
#         vehicle.start()
#         vehicle.stop()
#     else:
#             raise Exception ("It not a car and not a Motorcycle")