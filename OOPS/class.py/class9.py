#ENCAPSULATION
'''It is the process of binding the properties and the methods under one roof'''
#Abstraction:
'''Abstraction is used to hide the internal functionalities of the method from the user'''
'''The user only interact with basic implementations of the method ,but inner working is hidden'''
'''Python doesn't provide abstract class itself ,we need to import the abs module which provide the base for 
defining Abstract Base Classes [ABC]'''
'''Abstract class is a class with one (or) more abstract methods '''
'''Abstract method is a method with no implimentations '''
#SIMPLE EXAMPLE
from abc import ABC,abstractmethod
class TimeTable(ABC):
    @abstractmethod
    def breakfast(self):
        pass
    @abstractmethod
    def lunch(self):
        pass
    @abstractmethod
    def dinner(self):
        pass
class vamsikrishna(TimeTable):
    def breakfast(self):
        print('Eat Chicken Biriyani')
    def lunch(self):
        print('Eat Mutton Biriyani')
    def dinner(self):
        print('Drink cooldrink')
h=vamsikrishna()
h.breakfast()
h.lunch()
h.dinner()