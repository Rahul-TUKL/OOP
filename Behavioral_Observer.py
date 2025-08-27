# Observer Pattern : Treating main data source as a subject and all other dependedents as observers and maintaioning them as a list.
# class sheet2:
#     def __init__(self):
#         self.total = 0

#     def calculate_total(self, values: list[float]):
#         for value in values:
#             self.total += value
#             print(f"The total is {self.total}")
#         return self.total

# class barchart(): 
#     def create_bar(self, values:list[float]):
#         print(f"creating bar chart from {values}")    

# class DataSource:
#     def __init__(self):
#         self._values: list[float] = []
#         self.dependents:list[object] =[] # Single responsibility violations
    
#     @property
#     def values(self):
#         return self._values
    
#     @values.setter
#     def values(self, new_values:list[float]) -> None:
#         self._values = new_values

#         #update dependencies
#         for dependent in self.dependents:
#             if isinstance(dependent, sheet2):
#                 dependent.calculate_total(self._values)
#             if isinstance(dependent,barchart):
#                 dependent.create_bar(self._values) # Open Closed Principle Violations

#     def add_dependent(self, dependent: object):
#             self.dependents.append(dependent)

#     def remove_dependents(self, dependent: object):
#             self.dependents.append(dependent)

# Sheet2 =sheet2()
# Barchart =barchart()
# data_source = DataSource()
# data_source.add_dependent(Barchart)
# data_source.add_dependent((Sheet2))
# data_source.values=[1,2,4,6.5]

from abc import ABC, abstractmethod

class Observer(ABC): # Abstract Observer Class
    @abstractmethod 
    def update(self) ->None:
        pass 

class sheet2(Observer):
    def __init__(self, data_source):
        self.total = 0
        self.data_source = data_source

    def update(self):
        self.total = self.calculate_total(self.data_source.values)

    def calculate_total(self, values: list[float]):
        for value in values:
            self.total += value
        print(f"The total is {self.total}")
        return self.total   
     
class barchart(Observer): 
    def __init__(self, data_source):
        self.data_source = data_source

    def update(self):
        print(f"creating bar chart from {self.data_source.values}") 
        
class subject:
    def __init__(self):
        self.observers:list[Observer] =[] 
    
    def add_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class DataSource(subject):
    def __init__(self):
        super().__init__()
        self._values: list[float]=[]
    
    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, new_values:list[float]) -> None:
        self._values = new_values
        super().notify_observers()

datasource = DataSource()
Sheet2= sheet2(datasource)
Barchart = barchart(datasource)
datasource.add_observer(Sheet2)
datasource.add_observer(Barchart)
datasource.values=[1,25,6,7.5]