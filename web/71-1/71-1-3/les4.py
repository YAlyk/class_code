# a = [4,6,7,3,1,-1,0,-20,35]
# a = tuple(map(lambda x: x**3, a))
# print(a)


# def test(a):
#     b =[]
#     for i in a:
#         b.append(i**3)
#     print(tuple(b))


# a = [4, 6, 7, 3, 1, -1, 0, -20, 35]
# test(a)


# def increase(num):
#     return num + 7

# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = map(increase, numbers)
# print(new_numbers)


# def increase(num):
#     return num + 7

# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = map(increase, numbers)
# for num in new_numbers:
#     print(num, end=' ')


# def increase(num):
#     return num + 7


# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = list(map(increase, numbers))
# print(new_numbers)


# def func(elem1, elem2, elem3):
#     return elem1 + elem2 + elem3


# numbers1 = [1, 2, 3, 4]
# numbers2 = [10, 20]
# numbers3 = [100, 200, 300, 400, 500]
# new_numbers = list(map(func, numbers1, numbers2, numbers3))
# print(new_numbers)


# pi = 3.14159265359
# print(pi)
# print(round(pi, 5))
# print(round(pi))
# print(round(pi, 50))

"""
ДЗ_1:
Исправьте следующий код программы, в переменной 𝑟𝑒𝑠𝑢𝑙𝑡1 должны быть 
значения 𝑐𝑖𝑟𝑐𝑙𝑒_𝑎𝑟𝑒𝑎𝑠, округленные до 1 знaка после запятой, а в 𝑟𝑒𝑠𝑢𝑙𝑡2, 
числа должны быть округлены до 1,2,3,4,5,6 знаков соответственно.
"""
# circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
# result1 = list(map(round, circle_areas))
# result2 = list(map(round, circle_areas))
# result3 = list(map(round, circle_areas))
# result4 = list(map(round, circle_areas))
# result5 = list(map(round, circle_areas))
# result6 = list(map(round, circle_areas))
# print(circle_areas)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
"""
готовый код должен быть к следующему занятию.
"""


# тернарный оператор
# [если истина] if [выражение] else [если ложь]

# x, y = 25, 50
# b = x if x < y else y
# print(b)


# def func(elem):
#     return elem > 0


# numbers = [-1, 2, -3, 4, 0, -20, 10]
# positive_numbers = list(filter(func, numbers))
# print(positive_numbers)

# def func(a, b):
#     s = a+b
#     if s % 10 > 5:
#         return 'a'
#     elif s % 10 <= 5:
#         return 'b'


# x = [5, 7, 3, 6, 8, 0, 3, 4, 7, 9, 0, 2]
# y = [9, 6, 3, 6, 8, 3, 6, 8, 4, 5, 7, 4]
# res = []
# for i in range(len(x)):
#     res.append(func(x[i], y[i]))
# print(res)


# res = list(map(lambda a, b: 'a' if (a+b) % 10 > 5 else 'b', x, y))
# print(res)


# def print_all(*args, sep=' ', end='\n'):
#     res = sep.join(map(str, args))
#     return res + end


# print(print_all(1, 2, 3, 4, sep='a', end='!'))  # ->  1a2a3a4!
# print(print_all(1, 2, 3, 4, end='##'))  # -> 1 2 3 4##
# print(print_all(1, 2, 3, 4, 5))  # -> 1 2 3 4 5


# def map_list(func, *args):
#     res = []
#     for iterator in args:
#         temp = []
#         for i in iterator:
#             temp.append(func(i))
#         res.append(temp)
#     return res

# a, b, c = [1, 2, 3, 4], [23, -1], [None, [25]]
# print(map_list(str, a, b, c))


"""
ДЗ_2:
Необходимо реализовать filter_list, принимающий функцию для выполнения func, произвольное количество позиционных аргументов, каждый из которых содержит контейнеры. Функция должна возвращать список, состоящий из списков, каждый элемент которого удовлетворяет условию из функции func.
numbers = lambda a: type(a) in (int, float)
"""


# def filter_list(func, *args):
#     pass


# a, b, c = [1, 2, 3, 4], [23, -1], [None, [25]]
# def numbers(a): return type(a) in (int, float)


# print(filter_list(numbers, a, b, c))

"""
вывод: [[1,2,3,4], [23,-1], []]

готовый код должен быть к следующему занятию.
"""



# import math
# import statistics


# numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
# result = any(map(lambda x: True if x > 10 else False, numbers))
# if result:
#     print('Все числа больше 10')
# else:
#     print('Хотя бы одно число меньше или равно 10')


# colors = ['red', 'green', 'blue']
# for index, value in enumerate(colors, 100):
#     print(index, value)


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql',
#               'select', 'update', 'exec', 'del', 'truncate']
#     for word in ignore:
#         if word in command:
#             return True
#     return False


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql',
#               'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda word: True if word in command else False, ignore))




# print(all(map(lambda x: True if x.isdigit() and int(x) <=255 else False, input().split('.'))))




"""
Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране в формате: 

<capital> is the capital of <country>, population equal <population> people.
Moscow is the capital of Russia, population equal 145934462 people.
"""
# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321,
#               67_886_011, 65_273_511, 1_380_004_385]
"""
готовый код должен быть к следующему занятию.
"""
