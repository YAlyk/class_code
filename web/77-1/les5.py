# from random import randint

# def data_generate(min_num, max_num, n):
#     data = [randint(min_num, max_num) for el in range(n)]

#     return data


# def average_fu(data):

#     return round(sum(data) / len(data), 3)


# def sigma(data):
#     summa = 0
#     av = average_fu(data)

#     for el in data:
#         summa += (el - av) ** 2

#     return round((summa / (len(data) - 1)) ** 0.5, 3)

# def z_scores(data):
#     av = average_fu(data)
#     sig = sigma(data)
#     print(av, sig)

#     loc_data = []
#     for el in data:
#         loc_data.append(round((el - av) / sig, 3))

#     return loc_data

# data = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
# data_2 = z_scores(data)

# print('До стандартизации')
# print('Данные:', data)
# print('Среднее:', average_fu(data))
# print('Стандартное отклонение', sigma(data))

# print('После стандартизации')
# print('Данные:', data_2)
# print('Среднее:', average_fu(data_2))
# print('Стандартное отклонение', sigma(data_2))


# import pandas
# import numpy


# input = numpy.array(['Jonh', 'Bran', 'Sam', 'Peter'])
# series_data = pandas.Series(input, index=[10, 11, 12, 13])
# # print(type(input))
# print(series_data)
# print(type(series_data))


# input = [['Jonh', 'Pune'], ['Bran', 'Mumbai'], ['Ann', 'Delphi']]
# data_frame = pandas.DataFrame(input, columns=['Name', 'City'], index=[1, 2, 3])
# print(data_frame)
# print(type(data_frame))


# import pandas
# import numpy
# input = {'Name': pandas.Series(['John', 'Bran', 'Caret', 'Joha', 'Sam']),
#          'Marks': pandas.Series([44, 48, 75, 33, 99]),
#          'Roll_num': pandas.Series([1, 2, 3, 4, 5])
#          }
# # Creating a DataFrame
# data_frame = pandas.DataFrame(input)
# print(data_frame.describe())


import matplotlib.pyplot as plt

# x = [1, 2, 4, 6, 8]
# y = [1, 4, 8, 12, 16]

# plt.scatter(x, y)
# plt.show()


# def y(x):
#     return x ** 2


# x_min = int(input())
# x_max = int(input())
# data_x = [x for x in range(x_min, x_max+1, 1)]
# data_y = list(map(y, data_x))

# plt.scatter(data_x,data_y)



plt.plot([4,7,3,6,1], 'ro')
plt.show()