# a = int(input('Введите число: '))
# if a > 10:
#     print('Вы ввели число больше десяти!')
# elif a == 10:
#     print('a равно 10!')
# else:
#     print('Вы ввели число меньше или равное десяти!')

# i = 10
# while i > 0:
#     if i == 6:
#         continue
#     print(i)
#     i-=1
# else:
#     print('цикл закончен')

# первое задание 1 вариант
# for i in range(0, 501, 2):
#     print(i)

# первое задание 2 вариант
# for i in range(0, 501, 1):
#     if i % 2 == 0:
#         print(i)

#задание 2 первый вариант
# n = int(input('введите чило: '))
# summa = 0
# for i in range(0, n+1, 1):
#     summa+=i
# print(summa)

#задание 2 второй вариант
# i = 0
# n = int(input('введите чило: '))
# summa = 0
# while i <=n:
#     summa+=i
#     i+=1
# print(summa)

#задание 3 
# while True:
#     a = int(input())
#     print(a**2)
#     otvet = input('Хотите ли продолжить?').lower()
#     if otvet == 'выйти':
#         break

# def slojenie(a, b):
#     c = a + b
#     return c

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# d = slojenie(a, b)
# print(d * 2)

# задание 1
# def sum_range(start,end):
#     summa = 0
#     if start>end:
#         for i in range(end, start+1):
#             summa+=i
#     else:
#         for i in range(start, end+1):
#             summa += i
#     return summa

# start = int(input())
# end = int(input())
# print(sum_range(start, end))

# a = []
# a.append(5)
# print(a)


# a = ()
# a.