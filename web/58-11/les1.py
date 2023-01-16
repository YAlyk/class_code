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


n = int(input()) # кол-во строк
m = int(input()) # кол-во столбцов
a=[[int(i) for i in input().split()[:m]] for j in range(n)]
s = 0 # итоговая сумма
for i in range(n):
    s+=a[i][i]
print(s)