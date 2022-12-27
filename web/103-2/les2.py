# a = input().split()
# for i in a:
#     print('*' * int(i))
# a = input("чиселки: ").split()
# [print("*"*int(i)) for i in a]


# print('Введите кол-во клиентов:')
# a=int(input())
# print('Поочерёдно вводите величину накоплений каждого из клиентов:')
# c=[]
# for i in range(a):
#     b=int(input())
#     c.append(b)
# for t in range(len(c)):
#     c[t]*=3
# print('Доходы клиентов составят:', *c)

import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()
x = np.linspace(0, 10, 50)
y1 = x
y2 = [i**2 for i in x]
plt.title('квадратичная зависимость: y1 = x, y2 = x ^2')

plt.xlabel('x')
plt.ylabel('y1, y2')
plt.grid()
plt.plot(x, y1, x, y2)
plt.show()
