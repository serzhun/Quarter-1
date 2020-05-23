# # task 1
# def my_function(num_1, num_2):
#     try:
#         num_1, num_2 = float(num_1), float(num_2)
#         answer = num_1 / num_2
#     except ValueError:
#         return 'Ошибка числа'
#     except ZeroDivisionError:
#         return 'Деление на ноль'
#     return answer

# task 2
def personal_info(**kwargs):
    return kwargs

print(personal_info(
    name=input('name'),
    surname=input('surname'),
    birthday=input('birthday'),
    city=input('city'),
    email=input('email'),
    phone=input('phone'),
))

# task 3
def my_function(num_1, num_2, num_3):
    try:
        my_list = [num_1, num_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'check number'
# task 4
def my_pow_func(x, y):
    try:
        answer = x ** y
    except TypeError:
        return 'Enter float'
    return answer

print(my_pow_func(10, -2))

# task 4/2
def my_pow_func(x, y):
    # y - целое отрицательное
    try:
        x, y = float(x), int(y)
        res = x
        for i in range(abs(y) - 1):
            res *= x
            return 1 / res
    except ValueError:
        return 'Check value'

# task 5
def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Enter numbers or q to exit: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
    print(result)

# task 6
def int_func(text):
    return text.title()

print(int_func('text'))

res_int_func = int_func('bla bla bla')
print(res_int_func)