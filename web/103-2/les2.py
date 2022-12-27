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


# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()
# x = np.linspace(0, 10, 50)
# y1 = x
# y2 = [i**2 for i in x]
# plt.title('квадратичная зависимость: y1 = x, y2 = x ^2')

# plt.xlabel('x')
# plt.ylabel('y1, y2')
# plt.grid()
# plt.plot(x, y1, x, y2)
# plt.show()


# x = np.linspace(0 ,10, 50)
# y1 = x
# y2 = [i**2 for i in x]
# # отрисовка границ графика
# plt.figure(figsize=(9,9))
# plt.subplot(2,1,1)
# plt.plot(x,y1)
# #задание заголовка главного
# plt.title('квадратичная зависимость: y1 = x, y2 = x ^2')
# # подпись
# # одпись axis
# plt.ylabel('y1', fontsize = 14)
# plt.ylabel('y2', fontsize=14)
# # отрисовка графика, если указывается True
# plt.grid(True)
# # построение второго графика
# plt.subplot(2,1,2)
# plt.plot(x, y2)
# plt.xlabel('x', fontsize=14)
# plt.ylabel('y2', fontsize=14)
# # отрисовка графика, если указывается True
# plt.grid(True)
# # отрисовка окна
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# fruits = ['apple', 'peach', 'orange', 'bannana', 'melon']
# counts = [34, 25, 43, 31, 17]
# # функция bar отвечает за построение стобчатых диаграмм
# plt.bar(fruits, counts)
# plt.title('фрукты!')
# plt.xlabel('фрукты')
# plt.ylabel('значения')
# plt.grid(True)
# отрисовка окна
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
plt.plot(x, y1, 'o-r', label='line 1')
plt.plot(x, y2, 'o-.g', label='line 2')
plt.legend()
plt.show()
