# Liskov Substitution Principle
# Objects of the Superclass should be replaceable with the objects of the sub-class without affecting 
# the correctness of the program
from abc import abstractmethod, ABC
class Shape(ABC): # Subclasses should behave in this way
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height: float = 0.0, width: float = 0.0):
        super().__init__()
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height*self.width

class Square(Shape):
    def __init__(self, side: float = 0.0):
        super().__init__()
        self.side = side

    def calculate_area(self):
        return self.side*self.side
    
rect =Rectangle(5,10)
# print(f"Area of Rectangle is {rect.calculate_area()}")

sqr =Square(5)
# print(f"Area of Rectangle is {sqr.calculate_area()}")

def return_area(shape:Shape):
    return shape.calculate_area()
print(return_area(sqr)) #LSP priciple satisfied

#************************************************BAD EXample***********************************************************************************
# from enum import Enum
# from abc import abstractmethod, ABC

# class Shape(ABC):
#     def calculate_area(self):
#         pass #should provid this behavior

# class Rectangle(Shape):
#     def __init__(self, height: float = 0.0, width: float = 0.0):
#         super().__init__()
#         self.height = height
#         self.width = width

#     @property
#     def height(self):
#         return self.height
    
#     @height.setter
#     def height(self, new_height:float):
#         self.height = new_height

#     @property
#     def width(self):
#         return self.width
    
#     @width.setter
#     def width(self, new_width:float):
#         self.height = new_width
    
#     def calculate_area(self):
#         return self.height*self.width

# class Square(Rectangle):
#     def __init__(self, side: float = 0):
#         super().__init__(side, side)
    
#     @Rectangle.width.setter
#     def width(self, width: float):
#         self._width =width
#         self._height=width

#     @Rectangle.height.setter
#     def height(self, height: float):
#         self._width =height
#         self._height=height
    
#     def calculate_area(self):
#         return self.height*self.width
