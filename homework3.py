list = [1, 2, 3, 4, 5]
list.append(6)
print(list)


list1 = [1, 2, 3, 4, 5]
ress = list1.pop(2)
print(f'Удаленный элемент списка - {ress}, обновленный список - {list1}')

list2 = ['Яблоко', "Банан", "Вишня"]
list2.remove("Банан")
list2.insert(1, "Персик")
print(list2)

list3 = [42, 13, 89, 7, 64, 22]
list3.sort(reverse=False)
print(f'По возрастанию - {list3}')
list3.sort(reverse=True)
print(f"По убыванию - {list3}")

list4 = [[1,2], [3, 4], [5, 6]]
vlozhenyi = [7, 8]
list4.append(vlozhenyi)
print(list4)









for num in range(1, 10):
    print(num)


for num1 in range(1, 100):
    if num1 % 3 == 0 and num1 % 5 == 0:
        print(num1)


for num2 in range(1, 100):
    if num2 % 3 == 0 and num2 % 9 == 0 and num2 % 2 == 0:
        print(num2)


num3 = 0
while num3 < 237:
    print(num3)
    num3 += 2 


my_string = "Ботнет IPStorm, в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
for i in my_string:
    if i.isdigit():
        num4 = int(i) * 2
        print(num4)

# если вы имели ввиду все число то увы я не смог сделать 
        