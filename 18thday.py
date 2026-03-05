class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_er(self):  #setter method
        return self.__name
    def set_age(self,age): #getter method 
        if isinstance(age,int):
            self.__age=age
            print(self.__age)
        else:
            print("age not found")


s=student("shivu",78)
s.set_age(7)

#method over loding 
class claculater:
    def add(self,a,b,c=0):
        print(a+b+c)

s=claculater()
s.add(6,7)
s.add(3,6,5)

#method over riding
class animal:
    def sound(self):
        print("animal mack sound ")
class dog(animal):
    def sound(self):
        print("dog sound 'boking' ")

dogs=dog()
dogs.sound()

#abstract methof 

from abc import ABC, abstractmethod

class vechile(ABC):
    @abstractmethod
    def start_engen(self):
        pass
class car(vechile):
    def __init__(self,names):
        self.names=names

    def start_engen(self):
        print(" start engin ")

b=car("BMW")
print(b.names)
