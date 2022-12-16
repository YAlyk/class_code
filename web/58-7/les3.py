# a = 'hello'
# b = 'привет'
# print(a+' '+b)
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(len(a))

# print('ура' not in 'муравей')

# print(chr(125))
# print(ord('%'))

# i = 0
# while i <=255:
#     print(chr(i))
#     i+=1

# a = 'привет'
# print(a[-1])

# one = input().lower()
# two = input().upper()
# print(one, two)
# if one[-1] == two[0]:
#     print('верно')
# else:
#     print('ошибка')

# a = 'qwertyu'
# print(a[::-1])

# while True:
#     a = input("Введите слово: ")
#     if len(a) < 8:
#         print('короткий')
#     else:
#         if '123' in a:
#             print('простой')
#         else:
#             print('ok')
#             break

# a = input().split()
# print(a)


a = input().split()
for i in a:
    print('*' * int(i))
