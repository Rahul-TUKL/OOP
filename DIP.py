# Dependency Inversion Principle (DIP)
# High-level modules should not dpend on low-level modules.
# Both Should depend on Abstractions.
#************************************************Good EXample***********************************************************************************
from abc import ABC, abstractmethod
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass
class BasicEngine(Engine):
    def start(self):
        print("Basic Engine started")

class AdvancedEngine(Engine):
    def start(self):    
        print("Advanced Engine started")

class Car:
    def __init__(self, engine:Engine): #low-level class instance as an input
        self.engine= engine
    def starting (self):    
        self.engine.start()
        print("The car has started")
engine = AdvancedEngine()
car =Car(engine) # dependency injection
car.starting()

#************************************************BAD EXample***********************************************************************************
# If teh application is related to the car's behavior then "Car" is a "High-level" class and Engine provides specific functionality to the car
# Engine is a "Low-level" Class

class Engine:
    def start(self):
        print("Engine has started")

class Car:
    def __init__(self):
        self.engine= Engine() # Tight Coupling
    def starting (self):    
        self.engine.start()
        print("The car has started")