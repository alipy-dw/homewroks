#1
# file = open('/home/hello/Рабочий стол/Homeworks/sdelanue/files/file.txt', 'r')
# print(file.read())
# file.close()

#2
# file = open('/home/hello/Рабочий стол/Homeworks/sdelanue/files/users.txt', 'r+')
# file.writelines([input('Введите Логин: '), '\n'])
# file.writelines(input('Введите Пароль: ')) 
# file.seek(0)
# # print(file.read())
# # file.close()

#3
# west = open('/home/hello/Рабочий стол/Homeworks/sdelanue/files/file.txt','r')
# read = west.read()
# west.close()
# if 'w' in read:
    # print('Да в этом тексте есть символ w')
# else:
    # print('Нет, в тексте нет w')

#4
# with open('python.txt', 'w') as file:
#     print(file.write('''Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
#     you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
#     but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.'''))
# o_word = []
# with open('python.txt', 'r') as file1:
#     for i in file1.read().split():
#         if 'o' in i:
#             o_word.append(i)
# print(o_word) #тут я не буду врать долго думал как его сделать и итоге не смог найти решение в вбил в чат гпт

#5 
# with open('python.txt', 'w') as file:
#     print(file.write(''' """
#     .detacilpmoc naht retteb si xelpmoC
#     .xelpmoc naht retteb si elpmiS
#     .ticilpmi naht retteb si ticilpxE
#     .ylgu naht retteb si lufituaeB
#     """'''))
#тут уже написал первую половину кода взяв пример из прошлого кода и оставшую часть сам уже
# file = open('python.txt', 'r')
# read = file.read()
# file.close()
# print(read[::-1])

#6
# file = open('file.txt', 'w+')
# file.write("""123
# aaa456
# fxdya 5 0 0""")
# file.seek(0)
# reading = file.read()
# file.close()
# 
# sum1 = []
# for i in reading:
    # if i.isdigit():
        # sum1.append(int(i))
# print(sum(sum1)) # Ураааа я сделал, с этим шестым нормально так замучился