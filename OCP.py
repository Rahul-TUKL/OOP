# Open/Cloased Principle (OCP)
# Software Entities (classes, modules, functions, etc.) should be open for extension but closed for modiifcation
# Inheritence and polymorphism 
from enum import Enum
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self)-> float:
        pass

class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius
    def calculate_area(self)-> float:
        return math.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width   

    def calculate_area(self)-> float:
        return self.height*self.width
    
class Triangle(Shape):
    def __init__(self,height, base):
        self.height = height
        self.base = base   

    def calculate_area(self)-> float:
        return self.height*self.base*0.5
    
circle = Circle(5)
rect = Rectangle(6,4)
traingle = Triangle(10, 6)
print(f"Calculate Area of a circle:{circle.calculate_area()}")
print(f"calculate area of a Rectangle: {rect.calculate_area()}")   
print(f"calculate area of a Rectangle: {traingle.calculate_area()}")   
   
#************************************************BAD EXample***********************************************************************************
# from enum import Enum
# import math
# class ShapeType(Enum):
#     CIRCLE = 'circle'
#     RECTANGLE = 'rectangle' #To add triangle we have to change code here

# class Shape:
#     def __init__(self, shape_type: ShapeType, radius:float=0 , height : float=0, width: float =0):
#         self.type =shape_type
#         self.radius =radius
#         self.height = height
#         self.width = width
    
#     def calculate_area(self)-> float:
#         if self.type == ShapeType.CIRCLE:
#             return math.pi*self.radius**2
#         elif self.type == ShapeType.RECTANGLE:
#             return self.height*self.width
#         else:
#             raise ValueError ("Not a Correct shape")

# circle = Shape(ShapeType.CIRCLE, radius=5)
# rect = Shape(ShapeType.RECTANGLE, height=4, width=6)

# print(f"Calculate Area of a circle:{circle.calculate_area()}")
# print(f"calculate area of a Rectangle: {rect.calculate_area()}")
