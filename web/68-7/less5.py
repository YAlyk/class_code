# n=int(input()) # кол-во строк
# m=int(input()) # кол-во столбцов
# a=[[int(i) for i in input().split()[:m]] for j in range(n)]

# m = a[0][0]
# for i in range(n):
#     for j in range(n):
#         if i > j and i < n-1-j or i>j and i>n-1-j:
#             if a[i][j] > m:
#                 m = a[i][j]
# print(m)

# def swap(a, i, j):
#     for row in a:
#         row[i], row[j] = row[j], row[i]
#     return a

# n, m=[int(k) for k in input().split()]
# a=[[int(j) for j in input().split()] for i in range(n)]
# i, j = [int(k) for k in input().split()]

# for row in swap(a, i, j):
#     print(' '.join([str(i) for i in row]))

# n=int(input()) # кол-во строк
# m=int(input()) # кол-во столбцов
# a=[[int(i) for i in input().split()[:m]] for j in range(n)]
# x_1 = int(input())
# x_2 = int(input())

# for i in range(n):
#     a[i][x_1], a[i][x_2] = a[i][x_2], a[i][x_1]
# for j in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()

# n=int(input('введите количество строк: '))
# m=int(input('введите количество столбцов: '))
# print('введите матрицу по строкам, каждую с новой строки: \n')
# a=[[int(i) for i in input().split()[:m]] for j in range(n)]
# x_1=int(input('первый столбец для обмена: '))
# x_2=int(input('второй столбец для обмена: '))
# for i in range(n):
#     a[i][x_1], a[i][x_2] = a[i][x_2], a[i][x_1]
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()

#     print(a[i][j] + " ")


from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

b = a
b.sort()
print(b)

for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)