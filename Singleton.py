# class and it should have only one instance

# from abc import ABCMeta, abstractmethod

# class Iperson(metaclass = ABCMeta):
#     @abstractmethod
#     def get_data():
#         pass

# class PersonSingleton(Iperson):
#     __insatnce =None
#     @staticmethod
#     def get_instance():
#         if PersonSingleton.__insatnce ==None:
#             PersonSingleton("Default Name", 0)

#*********************classic __new__************************************
# class tower():
#     __instance = None
#     def __new__(cls,  *args, **kwargs): # blank object raw memory
#         if cls.__instance is None: 
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
    
#     def __init__(self):
#         print("The object is initialised")

# t1 =tower()
# t2=tower()
#print(t1 is t2)

#****************************** Singleton with Meta classes***********************

# class SingletonMeta(type):
#     __instance = {}

#     def __call__(cls, *args, **kwds):
#         if cls not in cls.__instance:
#             cls.__instance[cls]=super().__call__(*args, **kwds)
#         return cls.__instance[cls]

# class Controltower(metaclass=SingletonMeta):
#     def __init__(self):
#         print("Iniitialised")

# t1 = Controltower()
# t2 = Controltower()
# print(t1 is t2)


class SingletonMeta(type):
    __instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.__instance:
            cls.__instance[cls]= super().__call__(*args, **kwds)
        return cls.__instance[cls]
    
class controltower(metaclass =SingletonMeta):
    def __init__(self):
        print("Initialised only once")

t1=controltower()
t2=controltower()
print(t1 is t2)

