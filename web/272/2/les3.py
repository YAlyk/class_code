# меры центральной тенденции
# a = [0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7]
# print('среднее значение', sum(a)/18)
# print('мода = 2')
# print('медиана = 2')

import statistics
import random
from collections import Counter
random.seed(100)


def sr(d):
    print('среднее значение:', sum(d)/n)


def median(d):
    index = n // 2
    if n % 2:
        print('медиана:', sorted(d)[index])
    else:
        print('медиана:', sum(sorted(d)[index-1:index+1])/2)


def mod(d):
    c = Counter(d)
    print('мода:', [k for k, v in c.items() if v == c.most_common(1)[0][1]])


def raz(d):
    print('размах:', max(d)-min(d))


def sigma(d):
    mean = sum(d) / n
    dev = [(x-mean) ** 2 for x in d]
    sig = sum(dev) / n
    print('генеральная дисперсия:', sig)


n = 1000
d = [random.randint(0, 30) for i in range(n)]


print('расчёт кастомных функций')
sr(d)
median(d)
mod(d)
print('расчёты модуля statistics')
print('среднее значение:', statistics.mean(d))
print('медиана:', statistics.median(d))
print('мода:', statistics.mode(d))
print('________________________')
raz(d)
sigma(d)
