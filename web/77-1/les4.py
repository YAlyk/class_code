# global data, columns
# columns = ('id', 'name', 'lastname', 'age', 'height', 'weight')
# data = []


# def read(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             line = line.split(', ')
#             line = (int(line[0]), line[1], line[2], int(
#                 line[3]), int(line[4]), int(line[5]))
#             if line not in data:
#                 data.append(line)


# def write(filename):
#     with open(filename, 'w') as file:
#         for line in data:
#             file.write(', '.join([str(i) for i in line])+'\n')


# def add(line: str):
#     line = line.split(', ')
#     line = (int(line[0]), line[1], line[2], int(
#         line[3]), int(line[4]), int(line[5]))
#     if line not in data:
#         data.append(line)


# def remove(key, value):
#     col = columns.index(key)
#     # print(col)
#     row = -1
#     for i in range(len(data)):
#         if data[i][col] == value:
#             row = i
#             break
#     if row == -1:
#         print('No matches found')
#     else:
#         data.pop(row)


# def print_data():
#     for line in data:
#         print(', '.join([str(i) for i in line]))


# read('input.txt')
# print_data()
# remove('id', 1)
# print_data()
# write('input.txt')

import statistics
import random
random.seed(100)
n = 1000
d = [random.randint(0, 30) for i in range(n)]

# # print(d)


# print(sum(d)/len(d))
# print(statistics.mean(d))

# print('__________________________')

# n = len(d)
# sr = n // 2
# if n % 2:
#     print(sorted(d)[sr])
# else:
#     print(sum(sorted(d)[sr-1:sr+1])/2)

# print(statistics.median(d))

# print('__________________________')

# max = -1
# for i in d:
#     COLsov = d.count(i)
#     if COLsov > max:
#         zn = i
#         max = COLsov
# print(zn)
# # print(max)


# print(statistics.mode(d))
# # print(statistics.multimode(d))


print(statistics.variance(d))  # для дисперсии генеральной совокупности
print(statistics.pvariance(d))  # для дисперсии выборки
