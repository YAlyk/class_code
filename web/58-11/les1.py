# a = [[2, 3], [5, 9]]
# a = 'hello'


# a = input().split(', ')
# print(len(a))


# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# s = 0
# for i in range(len(a)):
#     s = s+a[i][i]
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()
# print('След матрицы = ', s)

# M = 3
# N = 3
# sled = 0
# Matr = [[1, 4, 6],
#         [5, 7, 9],
#         [7, 8, 1]]
# for i in range(M):
#     for j in range(N):
#         if i == j:
#             sled += Matr[i][j]
# print(sled)


# M = 3
# N = 3
# sled = 0
# A = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12]]
# for i in range(M):
#     for j in range(N):
#         if i == j:
#             sled += A[i][j]
# print(sled)

# задание 1
# n = int(input()) # кол-во строк
# m = int(input()) # кол-во столбцов
# a=[[int(i) for i in input().split()[:m]] for j in range(n)]
# s = 0 # итоговая сумма
# for i in range(n):
#     s+=a[i][i]
# print(s)

# n = int(input('Введите размер квадратной матрицы:'))

# a = [[int(i) for i in input().split()[:n]]for j in range(n)]
# max = a[0][1]
# for i in range(n):
#     for j in range(n):
#         if i > j and a[i][j] > max:
#             max = a[i][j]
# print('Максимальное значение:', max)

# задание 2
# n = int(input())  # вводим размерность матрицы
# a = [[int(i) for i in input().split()[:n]] for j in range(n)]
# m = a[0][0]  # максимальный элемент по умолчанию 
# for i in range(n):
#     for j in range(n):
#         if i > j and i < n - 1 - j or i > j and i > n-1-j:
#             if a[i][j] > m:
#                 m = a[i][j]
# print(m)


# print('Введите количество строк и количество столбцов: ')
# n = int(input())
# m = int(input())
# a = [[int(i) for i in input().split()[:m]]for j in range(n)]
# print('Введите значение столбцов, которые нужно поменять')
# p = int(input())
# k = int(input())
# for i in range(n):
#     d = a[i][p]
#     a[i][p] = a[i][k]
#     a[i][k] = d
#     print(a[i])


# n = int(input())
# m = int(input())
# a = [[int(i) for i in input().split()[:m]]for j in range(n)]
# x_1 = int(input())
# x_2 = int(input())
# for i in range(n):
#     a[i][x_1], a[i][x_2] = a[i][x_2], a[i][x_1]
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()



# import matplotlib.pyplot  as plt
# import numpy as np
# x = np.linspace(0, 10, 50)
# y = x
# plt.title('Линейная зависимость y = x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.plot(x, y)
# plt.show()