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
#     if start > end:
#         for i in range(end, start):
#             c +=i
#     else:
#         for i in range(start, end):
#             c += i
#     return c

# # первый вариант main кода
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
