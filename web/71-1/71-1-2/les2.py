# try:
#     a = int(input('Введите на число:'))
# except (ValueError):
#     print('Введён текст, а не число!')
# except(ZeroDivisionError):
#     print('Деление на 0')


# try:
#     a = int(input())
#     print(a+2)
#     print(a**2)
#     print(a[1])
#     a=tuple(a)
#     print(a)
# except(TypeError):
#     print('TypeError')

# s = 0
# for i in range(1, 10, 2):
#     if i % 2 == 0:
#         s = s + i
# print(s)

# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))


# def quadratic_solve(a: float, b: float, c: float):
#     if c == 0 and a != 0:
#         return sorted([0, -b/a])
#     elif a == 0:
#         return [-c/b]
#     else:
#         d = b*b-4*a*c
#         if d == 0:
#             return [-b/(2*a)]
#         elif d > 0:
#             return sorted([(d**0.5)-b/(2*a), (-(d**0.5)-b)/(2*a)])


# def test():
#     tests = [[1, 1, -10]]
#     results = [-3.7015621187164243, 2.7015621187164243]
#     i = 1
#     for a in tests:
#         if quadratic_solve(a[0], a[1], a[2]) == results[i-1]:
#             print(f'Тест №{i} прошел успешно ')
#             i += 1
#         else:
#             print('Тест провален')

# test()