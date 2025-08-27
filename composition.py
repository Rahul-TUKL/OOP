#********************TIGHT COUPLING***********************************
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
    def start(self):
        print(f"Engine starting with {self.horse_power} HP")

class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels
    def rotate(self):
        print(f"Rotating {self.number_of_wheels} Wheels")

class Chassis:
    def support(self):
        print("Chassis is supporting the car")

class Seats:
    def __init__(self, number_of_seats):
        self.number_of_seats = number_of_seats
    def seats(self):
        print(f"Car has {self.number_of_seats} seats")

class car: # Composed of other classes
    def __init__(self, horse_power: int = 0, number_of_wheels: int = 0,  number_of_seats: int = 0):
        self.horse_power = horse_power
        self.number_of_wheels = number_of_wheels
        self.number_of_seats= number_of_seats
        self._engine = Engine(self.horse_power) # composed of # Car has Engine # Tight Coupling
        self._wheels = Wheels(self.number_of_wheels) # Car has Wheels
        self._chassis = Chassis() # Car has Chassis
        self._seats = Seats(self.number_of_seats) # Car has Seats

    def start(self):
        self._engine.start()
        self._wheels.rotate()
        self._chassis.support()
        self._seats.seats() 

# Car=car(850,4,5)
# Car.start()


#**********************LOOSE COUPLING*********************************
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
    def start(self):
        print(f"Engine starting with {self.horse_power} HP")

class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels
    def rotate(self):
        print(f"Rotating {self.number_of_wheels} Wheels")

class Chassis:
    def support(self):
        print("Chassis is supporting the car")

class Seats:
    def __init__(self, number_of_seats):
        self.number_of_seats = number_of_seats
    def seats(self):
        print(f"Car has {self.number_of_seats} seats")

class car: # Composed of other classes
    def __init__(self, engine : Engine = object, wheels: Wheels = object, 
                 chassis: Chassis = object, seats : Seats = object ):
        self._engine = engine # composed of # Car has Engine # Tight Coupling
        self._wheels = wheels # Car has Wheels
        self._chassis = chassis # Car has Chassis
        self._seats = seats  # Car has Seats

    def start(self):
        self._engine.start()
        self._wheels.rotate()
        self._chassis.support()
        self._seats.seats() 

engine=Engine(850)
wheels=Wheels(4)
chassis = Chassis()
seats=Seats(5)
Car=car(engine, wheels, chassis, seats)
Car.start()