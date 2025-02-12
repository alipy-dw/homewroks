str1 = (input('Введите что-то: '))
res = str1.upper()
print(f" Исходная строка - {str1} , строка после изменение регистра - {res} ")

str = input('Напишите сюда предложение: ')
res1 = str.replace(' ','-')
print(res1)

str2 = input('Введите слово без цифр: ')
print(str2.isalpha())

str3 = "тут при помощи дир"
print(dir(str3))

str4 = input('Введите сюда предложение: ')
print(str4[0]) 
print(str4[-1])
# я не понял как делать срез строки 
print(str4.swapcase())

'====================================='



num = int(input('Введите сюда любое число: '))
if num % 2 == 0:
    print(f"Число {num} четное")
else:
    print(f'Число {num} не четное')

# 2

num1 = int(input('Введите сюда любое число: '))
if num1 % 2 == 0:
    print(f"Число {num1} четное")
else:
    print(f'Число {num1} не четное')

if num1 % 3 == 0:
    print(f'Число {num1} делиться на три без остатка')
else:
    print(f'Число {num1} не делиться на три без остатка')
if num1 ** 2 > 1000:
    print(f'Число {num1} в квадрате больше 1000')
else:
    print(f'Число {num1} в квадрате меньше 1000')


# 3 
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a and b > 0 and a :
    print(f'Число {a} и {b} - положительные')
if not (a and b > 0):
    print(f'Число {a} и {b} - отрицательные')

# 4 
age = int(input('Введите свой возраст: '))
if age < 0 or age > 120:    
    print('Недопустимый возраст')
elif age <= 4:
    print('Ребенок')
elif age >= 18:
    print('Cовершенолетний')


# 5
x = 13
ress = x ** 2
print(ress == 172)
if ress < 172:
    print(ress ** 2)