class EmailService: #Abstraction # Hiding implementation details and showing only the necessary details 
    #if someone wnats to learn driving, there is no need to learn about the car architecture or engine but just the gas pedal and breakes.
    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authentication...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("sending email")
        self._disconnect_email()

    def _disconnect_email(self):
        print("disconnecting from email server...")

# server = EmailService()
# server.send_email()


# Abstract classes cannot be instanciated; Meant to be subclassed
# Abstarct Methods must be implemented; Concrete Methods are inherited
# Abstraction enables inheritence
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # No Implementation
    @abstractmethod
    def stop(self):
        pass
    def safety(self): # Concrete Method
        print("All Components are working correctly")

class Car (Vehicle):
    def __init__(self, brand: str):
        super().__init__()
        self.brand = brand
    def start(self):
        print(f"{self.brand} Car is starting")
        self.safety()
    def stop(self):
        print(f"{self.brand} Car is stopping")

class MotorCycle(Vehicle):
    def __init__(self, brand):
        super().__init__()
        self.brand= brand

    def start(self):
        print(f"{self.brand} Motor Cycle is starting")

    def stop(self):
        print(f"{self.brand} Motorcycle is stopping")

class Boat(Vehicle):
    def __init__(self, brand):
        super().__init__()
        self.brand= brand

    def start(self):
        print(f"{self.brand} Boat is starting")

    def stop(self):
        print(f"{self.brand} Boat is Stopping")

motorcycle = MotorCycle("BMW")
car = Car("Ford")
boat = Boat("Titanic")
motorcycle.start()
motorcycle.safety()
motorcycle.stop()