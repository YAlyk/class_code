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
#filter - работает только с функциями, которые возвращают bool type


def func(a, b):
    s = a+b
    if s % 10 > 5:
        return 'a'
    elif s % 10 <= 5:
        return 'b'


x = [5, 7, 3, 6, 8, 0, 3, 4, 7, 9, 0, 2]
y = [9, 6, 3, 6, 8, 3, 6, 8, 4, 5, 7, 4]
res = []
for i in range(len(x)):
    res.append(func(x[i], y[i]))
print(res)

res = list(map(lambda a,b: 'a' if (a+b)%10>65 else 'b', x,y))