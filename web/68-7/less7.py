
# s = 0
# for i in range(1, 10, 2):
#     if i % 2 == 0:
#         s = s + i
# print(s)

# 


# def mult(a, b):
#     if a > b:
#         a, b = b, a
#     else:
#         return a**b


# a, b = 10, 2
# for i in range(1, 10):
#     b = a
#     b = mult(a, b)
# print(a, b)

# try:
#     print(t)  # NameError
#     list = [1, 2, 3, 4, 5]
#     print(list[122])  # IndexError
#     print(10/0)  # ZeroDivisionError
# except (NameError, IndexError, ZeroDivisionError):
#     print('В коде ошибки: NameError, IndexError, ZeroDivisionError')eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


import math

def quadratic_solve(a: float, b: float, c: float):

    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))

    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")


def test():
    tests = [

        [1, 1, -10],
        [1, 3, 13],
        [1, 23, 12],

    ]

    results = [

        [-3.7015621187164243, 2.7015621187164243]


    ]
    i = 1
    for a in tests:
        if quadratic_solve(a[0], a[1], a[2]) == results[i-1]:
            print(f'Тест №{i} прошел успешно')

    i += 1


test()
