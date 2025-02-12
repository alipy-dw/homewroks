# def zaim():
    # summa = int(input('Введите сумму (не менее 100000): '))
    # if summa < 100000:
        # print('Минимум 100000!')
    # else:
        # res = (summa / 100) * 7.89
        # return (f'Не обходимо вернуть {res + summa}')
# print(zaim())
# я не знаю как сделать так что бы округлял до двух чисел после запятой


# def zapros():
    # stroka = input('Введите числа и текст: ')
    # digit = ''
    # for i in stroka:
        # if i.isdigit():
            # digit += i
    # return(digit)
# print(zapros())


# def schestchik():
    # let = int(input("Введите сколько вам лет: "))
    # mounth = int(input('Введите сколько месяцев вы прожили с момента вашего др: '))
    # dni = let * 12 * 30
    # dni2 = mounth * 30
    # dni3 = dni + dni2
    # return dni3
# print(schestchik())


# def slovar():
    # dict = {i:i**3 for i in range(1,10)} # тут я уже через дикт комп
    # return dict
# print(slovar())

def numbers():
    return sum(range(1, 51)) #тут я спросил как можно было бы сложить все числа быстро, и чат гпт выдал это мне
res = numbers()
print(f'Сумма чисел от 1 до 50: {res}')