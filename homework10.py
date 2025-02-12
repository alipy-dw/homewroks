# names = ['Nikita', 'Katana', 'Toma']
# ages = [25, 30, 35]
# zipped = zip(names, ages)
# print(dict(zipped))



# text = "python"
# enum = enumerate(text, 1)
# for i in enum:
#     print(i)




# numbers = ["10", "20", "30", "40"]
# mapped = map(int, numbers)
# print(list(mapped))



# words = ["apple", "banana", "cherry", "dog", "elephant"]
# def filtere(n):
#     if n[0] == 'd':
#         return n
# filtered = filter(filtere, words)
# print(list(filtered))



# numbers = [1, -2, 3, -4, 5, -6]
# filtered1 = filter(lambda x: x > 0, numbers)
# print(list(map(lambda x:x ** 2, filtered1)))





students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
zipped1 = list(zip(students, scores))
def bolshe80(n):
    students, scores = n
    return scores > 80

filtered2 = filter(bolshe80, zipped1)
enumarated = list(enumerate(filtered2, 1))
print(list(enumarated))
