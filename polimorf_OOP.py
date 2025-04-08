#1
class Document:
    def print_info(self):
        pass

class PDFDocument(Document):
    def print_info(self):
        print('это - PDFDocument')

class WordDocument(Document):
    def print_info(self):
        print('это - WordDocument')

def print_document_info(docs):
    docs.print_info()

documents = [PDFDocument(),WordDocument(),WordDocument(),PDFDocument()]
for i in documents:
    print_document_info(docs=i)

#2
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Гав - гав')

class Cat(Animal):
    def make_sound(self):
        print('Мяу - мяу')

class Cow(Animal):
    def make_sound(self):
        print('Мууууууууууууууууууууууууууууууууууууууу')

ani = [Dog(), Cat(), Cow()]

def make_animals_talk(animals):
    for i in animals:
        i.make_sound()

make_animals_talk(ani)

#3
class Toy:
    def play_sound(self):
        pass

class Car(Toy):
    def play_sound(self):
        print('[Car] я Bugatti Chiron Super Sport 300+, дорогая игрушка\n')
    
class Doll(Toy):
    def play_sound(self):
        print('[Doll] Поиграй со мной!\n')
    
class Drum(Toy):
    def play_sound(self):
        print('[Drum] 3... 2... 1... БУМ!\n')

toys = [Car(), Doll(), Drum()]

def choose():
    print('Здравствуйте, вы в магазине <<Игромание>>!')
    while True:
        response = int(input('Выберите действие:\n1. Посмотреть игрушки\n2. Выйти из магазина\n\nOтвет: '))
        if response == 1:
            for i in toys:
                i.play_sound()
        else:
            print('Досвидание!')
            break

choose()

#4
from math import pi
class Shape:
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f'Площадь круга - {pi * self.radius ** 2}')

class Rectangle(Shape):
    def __init__(self, width, width2):
        self.width = width
        self.width2 = width2
    def area(self):
        print(f'Площадь прямоугольника - {self.width * self.width2}')

class Triangel(Shape):
    def __init__(self, a, height):
        self.a = a
        self.height = height
    def area(self):
        print(f'Площадь треугольника - {0,5 * self.a * self.height}')# тут у меня явно ошибка, наверное в формуле так как на выходе там не так правильно

shapes = [Circle(5), Rectangle(4, 6), Triangel(3, 8)]

for i in shapes:
    i.area()

#5
class Card:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        pass

class CreditCard(Card):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit
    def withdraw(self, amount):
        if self.balance - amount >= self.limit:
            self.balance -= amount
        else:
            print('Превышен лимит!')

class DebitCard(Card):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Недостаточно средтсв')

def snyatie_func(card, amount):
    card.withdraw(amount)

credit = CreditCard(balance=10000, limit=-1000)
debit = DebitCard(balance=10000)

snyatie = [(credit, 11000), (debit, 10000), (credit, 1), (debit, 1)]
for a, b in snyatie:
    snyatie_func(a, b)