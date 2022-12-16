# a = 1
# while a <= 500:
#     if a % 2 == 0:
#         print(a)
#     a += 1


# for a in range(1, 500, 1):
#     if a % 2 == 0:
#         print(a)
#     a += 1


# def myfunk():
#     global x, y
#     c = x + y
#     print(c)


# global x, y
# x = int(input())
# y = int(input())
# myfunk()
# # print(i)


# def check(login, password):
#     user_login = 'spiderman'
#     user_password = '#1$$$'
#     if user_login == login:
#         if user_password == password:
#             print('Вы вошли в систему')
#         else:
#             print('Неправильный пароль')
#     else:
#         print('Неправильный логин')


# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# check(login, password)


# def check(login, password):
#     user_login = 'spiderman'
#     user_password = '#1$$$'
#     if user_login == login and user_password == password:
#         print('вы вошли в систему')
#     else:
#         print('неверный логин или пароль')


# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# check(login, password)


# def sum_range(start, end):
#     sum = 0

#     if start > end:
#         for i in range(end, start + 1):
#             sum += i
#     else:
#         for i in range(start, end + 1):
#             sum += i
#     print(sum)


# start = int(input())
# end = int(input())
# sum_range(start, end)

# height = int(input())


# def triangle(height):
#     a = height - 1
#     b = 1
#     for i in range(height):
#         print(' ' * a + '^' * b)
#         a -= 1
#         b += 2


# triangle(height)
