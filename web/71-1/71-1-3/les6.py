# hello = input()
# print(f"{len(hello)*60//100} р. {len(hello)*60%100} коп.")
# rub = len(hello)*60//100
# kop = len(hello)*60 % 100
# ou = rub, 'р.', kop, 'коп.'
# print(rub, 'р.', kop, 'коп.')


# def one(x, y):return x + y

# a = [ '5', '9']
# b = list(map(int, a))
# print(b)
# print(type(b))

# def increase(num):
#     return num + 7


# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = map(increase, numbers)
# for num in new_numbers:
#     print(num, end=', ', sep=' ')

# print('text1','text2', 'text3', sep='/', end='|')


# тернарный оператор
# [если истина] if [выражение] else [если ложь]
# x, y = 25, 50
# b = x if x < y else y
# print(b)

# if x < y:
#     b = x
# else:
#     b = y
# print(b)

# def test(*args):
#     print(args)


# test('text','ещё текст', "и ещё текст")
# test(1525)
# test(True)

# def read_csv(filename):
#     data = {}
#     with open(filename, 'r') as file:
#         columns = tuple(file.readline().replace('\n', '').split(','))[1:]
#         # print(columns)
#         data = {i: [] for i in columns}
#         for line in file:
#             line = line.split(',')[1:]
#             for col, value in zip(columns, line):
#                 #print(col, value)
#                 value = value.replace('\n', '')
#                 value = int(value) if value.isdigit() else value
#                 data[col].append(value)
#     return data

# data = read_csv(r'web\71-1\71-1-3\countries.csv')
# print(data)


import json


def task1(data: json):
    for group in data:
        for student in data[group]:
            print(student['name'], student['lastname'], student['gpa'])


data = json.load(open(r'web\71-1\71-1-3\task.json'))
# for g in data:
#     for a in data[g]:
#         print(a)

# Анна Королёва 15 4.3
# task1(data)

res = {g: [] for g in data}
for g in data:
    for student in data[g]:
        res[g].append(student['gpa'])
# print(res)
for i in res:
    res[i] = sum(res[i])/len(res[i])
json.dump(res, open('result.json', 'w'))
