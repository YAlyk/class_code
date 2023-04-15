# тернарная операция, map, json.

# a = 10
# b = 5
# if a > b:
#     c = a
# else:
#     c = b
# print(c)

# #  <значение> if (условние) else <значение>
# c = a if a > b else b

# print(c)

# def pw(a):
#     return a**2


# a = [1, 5, 9, 6, 8]
# print(list(map(float, a)))


# a = [1, 5, 9, 6, 8]
# print(list(map(lambda x: x**2, a)))


# old_list = [1, 5, 9, 6, 8]
# new_list = []
# for item in old_list:
#     new_list.append(pw(item))
# print(new_list)


# def func(elem):
#     return elem > 0


# numbers = [-1, 2, -3, 4, 0, -20, 10]
# positive_numbers = list(filter(func, numbers))
# print(positive_numbers)

# map - работает со всеми функциями (базовыми и рукописными)
# filter - работает только с функциями, которые возвращают bool type


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

# res = list(map(lambda a, b: 'a' if (a+b) % 10 > 65 else 'b', x, y))


# def print_all(*args, sep=' ', end='\n'):
#     res = sep.join(map(str, args))
#     return res+end


# print(print_all(1, 2, 3, 4, sep='a', end='!'))  # -> '1a2a3a4!'
# print(print_all(1, 2, 3, 4, end='##'))  # -> '1 2 3 4##'
# print(print_all(1, 2, 3, 4, 5))  # -> '1 2 3 4 5'


# numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
# result = all(map(lambda x: True if x > 10 else False, numbers))
# if result:
#     print('Все числа больше 10')
# else:
#     print('Хотя бы одно число меньше или равно 10')


# colors = ['red', 'green', 'blue']
# for pair in enumerate(colors):
#     print(pair, type(pair))


# numbers = [1, 2, 3, 4]
# words = ['one', 'two', 'three']
# for pair in zip(numbers, words):
#     print(pair)


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


import json

def tasck1(data:json):
    for group in data:
        for student in data[group]:
            print(student['name'], student['lastname'], student['gpa'])
def pr(data):
    for g in data:
        for a in data[g]:
            print(a)


data = json.load(open(r'web\84-1\task.json'))

# tasck1(data)

res = {g:[] for g in data}
for g in data:
    for student in data[g]:
        res[g].append(student['gpa'])
for i in res:
    res[i] = sum(res[i])/len(res[i])
json.dump(res,open('result.json','w'))