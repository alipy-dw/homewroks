# try:
    # ...
# except SyntaxError:
    # print
# else:
    # print
# finally:
    # print


# try:
    # print(name)
# except NameError:
    # print('Такой переменной не сущетсвует')


# try:
    # nol = int(input('Введите число: '))
    # # nol1 = int(input('Введите второe число(не ноль пж): '))
    # res = nol / nol1
# except ZeroDivisionError:
    # print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!!')

# try:
    # num1 = int(input('Введите число: '))
    # num2 = int(input('Введите второе число: '))
    # num3 = num1 + num2
    # print(num3)
# except ValueError:
    # print('Введите число!')

# dict = {i:i**2 for i in range(2,6)}
# try:
    # print(dict[2])
# except KeyError:
    # print('Нет тaкого ключа!')

#тут я хотел опробовать через дикт комп


#6
# list = ['me', 'who?', 'where?', 'when?', 'who with?']
# try:
    # print(list[5])
# except IndexError:
    # print('Нет такого элемента!')


#7
# try:
    # age = int(input('Введите возраст: '))
    # if age < 18:
        # print('Некорректный возраст')
        # raise ValueError
    # else:
        # print('Спасибо')
# except ValueError:
    # print('Доступ запрещён')
# 
# finally:
    # print("До свидания!")

#8
# try:
    # num4 = int(input('Введите число: '))
    # num5 = int(input('Введите число: '))
    # ress = num4 / num5
    # print(ress)
# except (ZeroDivisionError, ValueError):
    # print('Произошла ошибка!')

#9
# try: 
    # money = int(input("Введите сумму денег: "))
    # if money < 0:
        # raise ValueError("Сумма не  может быть отрицательной!")
    # print(f'Выведена сумма: {money}')
# except ValueError as g:
    # print(f"Ошибка: {g}")

#10
# try:
    # ress1 = 'chislo' + 666
    # print(ress1) #наверное он сюда вовсе не нужен но я на всякий  оставил 
# except TypeError:
    # print('unsupported option')