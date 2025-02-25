#1
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print('Выполнение функции...')
#         res = func(*args,**kwargs)
#         return res
#     return wrapper
# @decorator
# def func(x, y):
#     return x + y

# ress = func(4,5)
# print(ress)

#2
# def decorator1(func):
    # def wrapper(*args,**kwargs):
        # res = func(*args,**kwargs)
        # return res * 2
    # return wrapper
# 
# @decorator1
# def func(x, y):
    # return x / y 
# 
# ress1 = func(100, 2)
# print(ress1)

#3
# def decor(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res + '!'
#     return wrapper

# @decor
# def func(x):
#     return x

# ress = func(input('Введите Что нибудь: '))
# print(ress)

#4
# def decor1(func):
#     count = 0
#     def wrapper(*args,**kwargs):
#         nonlocal count
#         if count < 3:
#             count += 1
#             res = func(*args,**kwargs)
#             return res + ', рад знакомсву!'
#         else:
#             print('Упс, моя радость исчерпалось. Досвидание!') #Ну или можно было так: "Функция больше недоступна"
#     return wrapper

# @decor1
# def func(x):
#     return x

# print(func(input('Введите своё имя: ')))
# print(func(input('Введите еще одно имя: ')))
# print(func(input('Введите имя еще раз: ')))
# func(input('Введите имя еще раз и это последний раз: '))

#5
# def decor2(func):
#     def wrapper(*args,**kwargs):
#         print(*args,**kwargs)
#         return func(*args,**kwargs)
#     return wrapper
# @decor2
# def func(x, y):
#     return x + y

# print(func(int(input('Введите число первое: ')),int(input('Введите число второе: '))))





