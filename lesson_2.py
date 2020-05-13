# # Task 1
# some_var = ('123', 123, [123], 123.0, False)
# for i in some_var:
#     print(type(i))
#
# # Task 2
# my_list = list(input('Enter text '))
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
#
# print(my_list)
#
# # Task 3 Var#1
# seasons_dict = {
#     1: 'Winter',
#     2: 'Winter',
#     3: 'Spring',
#     4: 'Spring',
#     5: 'Spring',
#     6: 'Summer',
#     7: 'Summer',
#     8: 'Summer',
#     9: 'Autumn',
#     10: 'Autumn',
#     11: 'Autumn',
#     12: 'Winter',
# }
# month = int(input('Enter month: '))
# print(seasons_dict[month])
#
# # Task 3 Var#2
# seasons_list = ['',
#                 'Winter',
#                 'Winter',
#                 'Spring',
#                 'Spring',
#                 'Spring',
#                 'Summer',
#                 'Summer',
#                 'Summer',
#                 'Autumn',
#                 'Autumn',
#                 'Autumn',
#                 'Winter']
# month = int(input('Enter month: '))
# print(seasons_list[month])
#
# # Task 4
# line = input()
# words = line.split()
# for i, word in enumerate(words):
#     print(i, word[:10])
#
# # Task 5
# my_list = [7, 5, 3, 3, 2]
# request = input('Enter int: ')
# for index, number in enumerate(my_list):
#     if int(request) < int(number):
#         continue
#     my_list.insert(index, request)
#     print(my_list)
#     break
# else:
#     my_list.append(request)
#     print(my_list)

# # Task 6
# goods = []
# features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
# analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
# num = 0
# while True:
#     if input('Exit - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
#         break
#     num += 1
#     for f in features.keys():
#         user_data = input('{}: '.format(f))
#         features[f] = int(user_data) if (f == 'цена' or f == 'количество')else user_data
#         analitics[f].append(features[f])
#         goods.append((num, fuatures))
#         print('Текущая аналитика по товарам: \n')
#         for key, value in analitics.items():
#             print(key, value)
