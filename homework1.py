num1 = int(input('Введите любое первое число: '))
num2 = int(input('Введите любое второе число: '))
res = num1 + num2 
res2 = res * 7 
res3 = res2 ** 2
res4 = res3 - 5555
print(res4)

'=============================='

str1 = int(input('Ваш год рождения: '))
num_now = 2025 
num2yago = 2023
num2yafter = 2027
age1 = num_now - str1
age2 = num2yago - str1
age3 = num2yafter - str1
print(f'Ваш возраст: {age1}', f'Ваш возраст два года назад: {age2}', f'Ваш возраст через два года: {age3}')
num365 = age1 * 365
print(num365)

'=============================='

age = int(input('Ваш возраст: '))
sec = age * 365 * 24 * 60 * 60
print(f'Возраст человека - {age}, количество секунд прожито - {sec}')

'======================================'

chocolate = int(input('Стоимость шоколода: '))
milk = int(input('Стоимость молока: '))
coffe = int(input('Стоимость кофе: '))
chocolate_1 = int(input('Количество шоколада: '))
milk_1 = int(input("Количество молока: "))
coffe_1 = int(input("Количество кофе: "))
vse = (chocolate * chocolate_1) + (milk * milk_1) + (coffe * coffe_1)
print(f'Стоимость товаров в корзине:{vse}')

'================================='


dlina = int(input("Длина прямоугольника (м): "))
shirina = int(input("Ширина прямоугольника (м): "))
perimetr = 2 * (shirina + dlina)
print(f'Периметр прямоугольника равен: {perimetr}')



# надеюсь что все ок
# вы же можете каждый блок по отдельности рассматривать 
