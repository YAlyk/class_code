
# первое задание
# n = int(input()) # кол-во строк
# m = int(input()) # кол-во столбцов
# a = [[int(i) for i in input().split()[:m]] for j in range(n)]
# s = 0
# for i in range(n):
#     s += a[i][i]
# print(s)


# второе задание
# n = int(input('Введите размерность матрицы: '))
# a = [[int(i) for i in input().split()[:n]] for j in range(n)]
# m = a[0][0]
# for i in range(n):
#     for j in range(n):
#         if i > j and i < n-1-j or i > j and i > n-1-j:
#             if a[i][j] > m:
#                 m = a[i][j]
# print(m)


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)

# fig.set(facecolor = 'green')
# ax.set(facecolor = 'red')

fig.set_facecolor('green')
ax.set_facecolor('gray')
plt.show()
