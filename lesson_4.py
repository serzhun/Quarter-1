# task 1
import sys

hours, salary_per_our, bonus = map(float, sys.argv[1:])
print('Salary - {}'.format(hours * salary_per_our + bonus))

# task 2
my_list = [1, 9, 1, 72, 3, 4, 5, 6, 3]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1]  and i != 0]
print(new_list)

# task 3
print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])

# task 4
my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
new_list = [x for x in my_list if my_list.count(x) == 1]

# task 5
from functools import reduce

def mul_list(n1, n2):
    return n1 * n2

my_list = [x for x in range(100, 1001) if x % 2 == 0]
reduce(mul_list, my_list)

#task 6
from itertools import count, cycle

for i in count(int(input('Enter your int: '))):
    print(i)

#task 6/1
my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]

iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
    stop = input()

#task 7
from math import factorial
from itertools import count

def fibo_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fibo_gen():
    print('Factorial {} - {}'.format(x + 1, i))
    if x == 14:
        break
    x += 1