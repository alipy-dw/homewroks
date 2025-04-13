#1
class Team:
    def __init__(self, team):
        self.team = team
        self.team_group = []
    def add_player(self,player):
        self.team_group.append(player)
    def show_team(self):
        print(f'Players in team:\n')
        for i in self.team_group:
            print(i.name)

class Player:
    def __init__(self, name):
        self.name = name

Alice = Player('Alice')
bob = Player('BOB')
team = Team('Players')
team.add_player(Alice)
team.add_player(bob)
team.show_team()

#2
class CompanyA:
    def add_employee(self,person):
        self.employess = []
        self.employess.append(person)

    def show_employees(self):
        print('Employees in Company A:')
        for i in self.employess:
            print(i.name)

class CompanyB:
    def add_employee(self,person):
        self.employess = []
        self.employess.append(person)

    def show_employees(self):
        print('Employees in Company B:')
        for i in self.employess:
            print(i.name)

class Employe:
    def __init__(self, name):
        self.name = name

John = Employe('John')
company1 = CompanyA()
compani2 = CompanyB()
company1.add_employee(John)
compani2.add_employee(John)
company1.show_employees()
compani2.show_employees()

#3
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Death_room"), Room("Livin_room")]
    def show_rooms(self):
        print(f'Number of rooms: {len(self.rooms)}')

house = House()
house.show_rooms()

4
class Page:
    def __init__(self):
        pass

class Book:
    def __init__(self):
        self.rooms = [Page(), Page(), Page()]
    def show_rooms(self):
        print(f'Pages in book: {len(self.rooms)}')

house = Book()
house.show_rooms()

#5
class RAM:
    def __init__(self, name):
        self.name = name
class CPU:
    def __init__(self, name):
        self.name = name
class Computer:
    def __init__(self):
        self.ram = RAM('16GB')
        self.gpu = CPU('Intel i7')

    def show_info(self):
        print(f'Computer has:\nCPU: {self.gpu.name}\nRAM: {self.ram.name}')

comp = Computer()
comp.show_info()

#6
class Playlist:
    def __init__(self, name):
        self.name = name

    def add_song(self, song):
        self.songs = []
        self.songs.append(song.name)

class Song:
    def __init__(self, name):
        self.name = name
    
    def play(self):
        print(self.name)

def proverka():
    if hasattr(See_You_Again, 'play'):
        print('Song still exists: True')

See_You_Again = Song('See_You_Again')
Tyler = Playlist('Tyler, The Creator')
Tyler.add_song(See_You_Again)
del Tyler
proverka()
#надеюсь правильно, дайте знать пожайлуста

class Paragraph:
    def __init__(self, name):
        self.name = name


class Document:
    def __init__(self):
        self.paragraphs = [
            Paragraph("first"),
            Paragraph("second"),
        ]

doc = Document()
paragraph_refs = doc.paragraphs # вот эту строку и последующие списал с чата сам не знал как решить

del doc

alive_paragraphs = [p for p in paragraph_refs if p is not None]
print("Paragraphs after document deletion:", len(alive_paragraphs))