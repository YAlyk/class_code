# a = 'hello world!'
# print(a[0])
# print(a[-5])
#   start stop step | пример среза
# print(a[0:5:])
# задание: вывести строку 'hello, world!'
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

from collections import namedtuple
marks = namedtuple('Marks', 'Physics Math Eng')
marks = marks(Physics=5, Math=4, Eng=5)
print(marks.Eng)
