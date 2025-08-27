# Interface Segregation Principle (ISP)
# Clients should not be forced to depend on interfaces they do not use
# If some function is not in use it should be removed
from abc import abstractmethod, ABC
import math

class Shape2d(ABC): # Subclasses should behave in this way
    @abstractmethod
    def calculate_area(self):
        pass

class shape3d(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod    
    def calculate_volume(self):
        pass

class Circle(Shape2d):
    def __init__(self, radius: float = 0.0):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return math.pi*self.radius**2
    
class Sphere(shape3d):
    def __init__(self, radius: float = 0.0):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 4*math.pi*self.radius**2
    
    def calculate_volume(self):
        return (4/3)*math.pi*self.radius**3    
    
circle = Circle(5)
sphere = Sphere(5)
print(f"Calculate Area of a circle:{circle.calculate_area()}")
print(f"calculate area of a Sphere: {sphere.calculate_volume()}")