# import Abstract Class Method
from abc import ABC, abstractmethod

# define an abstract class called Phones


class Phones(ABC):

    # define an abstract method
    @abstractmethod
    def printPhone(self):
        pass


class Iphone(Phones):

    # define a method
    def printPhone(self):
        print('this is an Iphone that is inferior to Androids')


class Android(Phones):

    # define a method
    def printPhone(self):
        print('This is an Android. Androids are superior to all Phones')


# created an Object
Techno = Android()

# print out the phone OP
Techno.printPhone()
