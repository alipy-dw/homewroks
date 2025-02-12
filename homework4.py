# pervyi sposob
# d = {
    # 'monday': 1,
    # 'thuesday': 2,
    # 'wendesday': 3,
    # 'thursday':4,
    # 'friday':5,
    # 'saturday':6,
    # 'sunday':7
# }
# print(d['wendesday'])

#vtoroi sposob
# d2 = dict(monday = 1,thuesday = 2,wendesday = 3, thursday = 4, friday=5, saturday=6, sunday=7 )
# print(d2['thuesday'])


#2
# week = {"понедельник":1, "вторник":2, "среда":3}
# print(week.get(input("Введите день: "), ("Такого дня нет")))

#3 
mounth = {}
# mounth["august"] = 31
# mounth["february"] = 29
# mounth["september"] = 30
# print(mounth)

#4
# grades = {"математика":5,"физика":4,"химия":3}
# grades2 = {"химия":4}
# grades.pop("химия")
# grades.update(grades2)
# print(grades)

#5
# subject = {"математика":5,"физика":4,"химия":3}
# subject.pop("физика") 
# print(subject)


#6
# products = {"яблоки": 50, "бананы": 30, "апельсины": 70}
# print(products.get(input("Введите название продукта: "), ("Товар отсутствует")))

#7
# config = {"theme": "dark", "version": "1.0.1", "debug": True}
# config_copied = config.copy()
# config_copied["debug"]= False
# print(config, config_copied)

#8
# phonebook = {"Иван": "123-45-67", "Мария": "789-01-23", "Олег": "456-78-90"}
# keys = phonebook.keys()
# print(list(keys))

#9
scores = {"Аня": 85, "Борис": 92, "Вика": 78, "Гена": 88}
for name, score in scores.items():
    print(f"{name} - {score}") 
