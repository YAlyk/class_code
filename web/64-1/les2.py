# a = int(input('Введите число: '))

# if a < 20:
#     print('число меньше 20ти')
# elif a <= 40:
#     print('число меньше 40ка')
# else:
#     print('Число больше 40')


# print('Начало отсчета!')

# i = 10
# while i >0:

#     if i == 5:
#         print('запуск!')
#         continue
#     else:
#         print('До запуска осталось:', i)
#     i -= 1
# else:
#     print('Запуск!')


# print('Начало отсчета!')
# for i in range(10, -1, -1):
#     print('До запуска осталось:', i)
# print('запуск!')

def MyFunck(x, y):
    w = x + y
    print('сумма a и b =', w)


def Vivod():
    print('Привет')


def Razn(q, e):
    return q - e


Vivod()
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

MyFunck(a, b)

w = Razn(a, b)
print('Разность a и b=', w)

# while True:
#     a = input('Введите число или прекратите работу программы введя %: ')
#     if a == '%':
#         break
#     else:
#         a = int(a)
#         print("Квадрат числа =", a**2)

# print('текст \nтекст с другой строки')
