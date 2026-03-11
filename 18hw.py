# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance

#     def geter_bal(self):
#         return self.__balance
    
#     def seter_bal(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             print("balense cann't be negative ")

    
# b=BankAccount(780)
# print(f"account balance is {b.geter_bal()}")

# b.seter_bal(788)
# print(f"update th balance {b.geter_bal()}")

# b.seter_bal(-678)

# #method over loading
# class Calculater:
#     def multipal(self,a,b,c=0):
#         print(a*b)
#         print(c*a,b)

# m=Calculater()
# m.multipal(5,8,9)


# #method overriding 
# class Shape():
#     def draw(self):
#         print("drawing shapes ")

# class circal(Shape):
#     def draw(self):
#         print("drawind a circal ")
# e=circal()
# e.draw()


# abstract method 
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class manager(Employee):
    def __init__(self,hous_work,rent_per_hor):
        self.hous_work=hous_work
        self.rent_per_hor=rent_per_hor

    def calculate_salary(self):
        return self.hous_work * self.rent_per_hor
    
manager1=manager(788,99)
print("manager rent is",manager1.calculate_salary())
