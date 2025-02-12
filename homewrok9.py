# def calculator():
#     try:
#         num1 = int(input('Введите число: '))
#         num2 = int(input('Введите число второе: '))
#     except ValueError:
#         print('Введите числа!')
#         return
#     operation = input('Введите операцию (+,-,*,/): ')
#     operations = {
#         '-' : lambda num1 , num2:num1 - num2,
#         '+' : lambda num1 , num2:num1 + num2,
#         '*' : lambda num1 , num2:num1 * num2,
#         '/' : lambda num1 , num2:num1 / num2 if num2 != 0 else 'Нельзя делить на ноль'
#     }
#     if operation not in operations:
#         print('Нет такой операции')
#         return
#     res = operations[operation](num1, num2)
#     if isinstance(res, str):
#         print(res)
#     else:
#         print(f'{res}')
# calculator()
