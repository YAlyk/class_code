# # def summa():
# #     c = a + b
# #     return c


# # global a, b
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # funk = summa()
# # w = funk * 2
# # print()

# # первый вариант функции
# def sum_range(start, end):
#     if start > end:
#         end, start = start, end
#     return sum(range(start, end + 1))

# # второй вариант функции
# def sum_range(start, end):
#     c = 0
#     a = 'text'
#     if start > end:
#         for i in range(end, start):
#             c +=i
#     else:
#         for i in range(start, end):
#             c += i
#     return c, a

# # # первый вариант main кода
# start = int(input('От: '))
# end = int(input('До: '))
# print('Сумма от', start, 'до', end, '=', sum_range(start, end))

# # второй вариант main кода
# start = int(input('От: '))
# end = int(input('До: '))
# if start > end:
#     print('Сумма от', start, 'до', end, '=', sum_range(end, start))
# else:
#     print('Сумма от', start, 'до', end, '=', sum_range(start, end))

# height = int(input('Введите высоту: '))
# for i in range(height):
#     print(' '*(height-i) + "*"*(i+1)+'*'*i)


# a = 'привет'
# c = 'привет, это строка со срезом!'
# b = 'hello'
# # print(a[-1])
# print(c[::-2])

# print(ord('%'))
# print(chr(109))

# a = ['apple', 'orange', 'mandarin']
# print(a)
# del a
# print(a)

# a = ('apple', 'orange', 'mandarin')

# a = {'apple', 'orange', 'mandarin', 'apple', 'orange', 'mandarin'}
# b = {'BMW', 'Merc', 'oka', 'apple'}
# print()
# print(a)
# print()
# a.update()


# a = {}