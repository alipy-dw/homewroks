from abc import abstractmethod, ABC
from math import pi

#1
class Transport(ABC):
    @abstractmethod
    def move(self):
        ...

class Car(Transport):
    def move(self):
        print('Car is moving on the road')

class Plane(Transport):
    def move(self):
        print('Plane is flying in the sky')

car = Car()
plane = Plane()
car.move()
plane.move()

#2
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        ...

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата {amount} через Credit Card')

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата {amount} через PayPal')

creditcard = CreditCard()
paypal = PayPal()
creditcard.pay(2345)
paypal.pay(6789)

#3
class Shape(ABC):
    @abstractmethod
    def area(self,value):
        ...

class Circle(Shape):
    def area(self, radius):
        print(f'Площадь круга - {pi * radius ** 2}')

class Rectangle(Shape):
    def area(self, width, width2):
        print(f'Площадь прямоугольника - {width * width2}')

cicle = Circle()
rectangle = Rectangle()
cicle.area(2)
rectangle.area(4, 50)

#4
class OutputDevice(ABC):
    @abstractmethod
    def display(self,text):
        ...

class Monitor(OutputDevice):
    def display(self, text):
        print(f'[Monitor] {text}')

class Printer(OutputDevice):
    def display(self, text):
        print(f'[Printer] {text}')

monitor = Monitor()
printer = Printer()
monitor.display('Hello Ali!')
printer.display('Hello Myself!')
# если сделал не так как надо дайте мне знать, пожалуйста

#5
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...

class Dog(Animal):
    def make_sound(self):
        print('Гав!')

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

#6
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        ...

class Developer(Employee):
    def calculate_salary(self, salary):
        print(f'Зарплата разработчика: {salary + 3000}')

class Manager(Employee):
    def calculate_salary(self, salary):
        print(f'Зарплата менеджера: {salary + 5000}')

dev = Developer()
man = Manager()
dev.calculate_salary(4000)
man.calculate_salary(4000)
# Если сделал не так как надо было, дайте знать

#7
class DataBase(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def disconnect(self):
        ...

class MySQLDatabase(DataBase):
    def connect(self):
        print('Подключение к MySQL')
    
    def disconnect(self):
        print('Отключение от MySQL')

class PostgreSQLDatabase(DataBase):
    def connect(self):
        print('Подключение к PostgreSQL')
    
    def disconnect(self):
        print('Отключение от PostgreSQL')

msql = MySQLDatabase()
sql = PostgreSQLDatabase()
msql.connect()
msql.disconnect()
sql.connect()
sql.disconnect()