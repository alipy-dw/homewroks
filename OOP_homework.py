#1
# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f'Баланс пополнен на {amount} соь')

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f'Вы сняли {amount} сом')
#         else:
#             print('Недостаточно средств')
    
#     def get_balance(self):
#         return self.__balance

# Client = BankAccount()
# Client.deposit(1000)
# Client.withdraw(500)
# print(Client.get_balance())

#2
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.__password = "ne_znyau17"
    
#     def get_password(self):
#         return '*' * len(self.__password)
    
#     def set_password(self, new_password):
#         if len(new_password) > 6:
#             self.__password = new_password

# account = User('Faha')
# print(account.name)
# print(account.get_password())
# account.set_password('faha2009')
# print(account.get_password())

#3
# class Employee:

#     def __init__(self, salary, name):
#         self.__salary = salary
#         self.name = name
    
#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self, salary):
#         if salary > 30000:
#             self.__salary = salary

# warrior = Employee('30000', 'Faha')
# warrior.set_salary(10000)
# print(warrior.get_salary())

#4
from math import pi
class Circle:
    
    def __init__(self, radius):
        self._radius = None
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, zhachenie):
        if zhachenie > 0:
            self._radius = zhachenie
        else:
            print("Радиус не меньше нуля!")
    
    def area(self):
        return pi * self._radius ** 2


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self._height = height

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,vysota):
        if vysota > 0:
            self._height = vysota
        else:
            print('Высота не может быть меньше нуля!')

krug = Circle(10)
print(krug.area())
print(krug.radius)

cylinder = Cylinder(5, 7)
print( cylinder.radius)   # ➤ 5
print( cylinder.height)   # ➤ 7
print( cylinder.area())
        