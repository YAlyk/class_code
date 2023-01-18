# a = 'hello world!'
# print(a[0])
# print(a[-5])
# #  start stop step | пример среза
# print(a[0:5:])
# # задание: вывести строку 'hello, world!'
# print(a[:5:]+','+a[5:12:])

# a = [1, 8, 6, -5, 6, 8, 6]
# b = [55, 28, 36]
# print(a)
# a.pop(-5)
# print(a)
# print(a.index(6))
# a.extend(b)
# print(a)
# print(a.count(6))
# a[2] = 3
# print(a)

# a = (1, 5, 9, -5, 55)

# from collections import namedtuple
# marks = namedtuple('Marks', 'Physics Math Eng')
# marks = marks(Physics=5, Math=4, Eng=5)
# print(marks)
# print(marks.Math)

# a = input().split()
# print(a)
# print(len(a))

# a = input().split()
# per_pol = a[:len(a)//2]
# vtor_pol = a[len(a)//2:]
# sr_per = sum(map(int, per_pol)) / len(per_pol)
# sr_vtor = sum(map(int, vtor_pol)) / len(vtor_pol)
# print('первое полугодие ср: ',  sr_per,
#       '\nвторое полугодие ср:', sr_vtor)

# a = input().split()
# for i in a:
#     print('*' * int(i))

# a = {2, 8, 555, 9, 10, 2, 6 }
# b = {'aplle', 'orange', 'mandarin', 'aplle'}
# c = {'aplle', 'google', 'facebook'}
# a.update(b)
# print(b | c)
# print(b & c)
# print(b - c)
# print(b ^ c)
# def test():
#     pass
# print(test)
