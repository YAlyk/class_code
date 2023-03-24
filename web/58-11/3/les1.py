# a = input('мпмпнмнп')
# p = 60 * len(a) // 100
# d = 60 * len(a) % 100
# print(p,'рублей', d, 'копеек')


# str = input()
# k = 0
# for i in range(len(str)-1):
#     if str[i] == str[i+1] == 'Р':
#         k += 1
# print(k+1)


# s = input()
# c, i = 0, 0
# while i < len(s):
#     if s[i] == 'P':
#         temp = 0
#         while i < len[s] and s[i] !='O':
#             temp+=1
#             i+=1
#         c=max(temp,c)
#     i+=1
# print(c)


# s = input()
# s = s.replace('OO', 'O')
# s = s.split('O')
# m = 0
# print(s)
# for i in s:
#     m = max(m, len(i))
# print(m)

from math import sqrt
import statistics as st
from random import *

n = 1000
seed(100)

a = [randint(0, 30) for i in range(n)]
len, sum = len(a), sum(a)
sum1 = 0
for i in a:
    sum1 += (i - sum / len)**2
total = sqrt(sum1)
print(total)
print(max(a)-min(a))
