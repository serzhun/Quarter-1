Lesson 1

# # Task 1
# a = 'hello'
# b = 'world'
# print(a, b)
# num = int(input())
# print('Вы ввели:  ', num)
#
# # Task 2
# time = int(input('Введите время в секундах:  '))
# hours = time // 3600
# minutes = (time // 60) - (hours * 60)
# seconds = time % 60
# print(f'{hours}:{minutes}:{seconds}')
#
# # Task 3
# n = input('Введите число: ')
# print(f'{n} + {n + n} + {n + n + n} + {int(n) + int(n + n) + int(n + n + n)}')
#
# # Task 4
# num_user = int(input('Enter int: '))
# current_max = 0
# num = num_user
#
# while num > 0:
#     digit = num % 10
#     if digit > current_max:
#         current_max = digit
#         if current_max == 9:
#             break
#     num = num // 10
#
# print('Наибольшая цифра у введенного числа: ', current_max)
#
# # Task 5
# revenue = float(input('Выручка: '))
# costs = float(input('Издержки: '))
#
# result = revenue - costs
#
# if result > 0:
#     print('Company is working with revenue', result)
#     print('Рентабельность: ', result / revenue)
#     people = int(input('численность сотрудников: '))
#     print(f'Прибыль на одного сотрудника: {result / people:.2f}')
# elif result < 0:
#     print('Company is working without revenue: ', result)
# else:
#     print('Компания работает в 0')

# Task 6
while True:
    days = 1
    start_km = int(input('Стартовый результат: '))
    last_km = int(input('Финальный результат: '))
    if start_km > last_km:
        print('Input incorrect data')
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print('Спортсмен добьется результата за {} дней'.format(days))
        break