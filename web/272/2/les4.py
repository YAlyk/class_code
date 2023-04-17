# from random import randint


# # генерация данных
# def data_generate(min_num, max_num, n):
#     data = [randint(min_num, max_num) for el in range(n)]

#     return data


# # среднее значение
# def average_fu(data):
#     return round(sum(data) / len(data), 3)


# # отклонение(сигма)
# def sigma(data):
#     summa = 0
#     av = average_fu(data)
#     for el in data:
#         summa += (el-av)**2

#     return round((summa/(len(data) - 1)) ** 0.5, 3)


# # стандартизация
# def z_scores(data):
#     av = average_fu(data)
#     sig = sigma(data)
#     print(av, sig)

#     loc_data = []
#     for el in data:
#         loc_data.append(round((el - av)/sig, 3))

#     return loc_data


# data = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
# data_2 = z_scores(data)

# print('До стандартизации.')
# print('Данные:', data)
# print('Ср знач:', average_fu(data))
# print('Стандартное отклонение:', sigma(data))

# print('После стандартизации.')
# print('Данные:', data_2)
# print('Ср знач:', average_fu(data_2))
# print('Стандартное отклонение:', sigma(data_2))




# import matplotlib.pyplot as plt

# def find_cnt(data:list)->dict:
#     dic = {}
#     for el in set(data):
#         dic[el] = data.count(el)
#     return dic

# def mode (data:dict)->dict:
#     max_el = max(data.values())
#     return {key: value for key, value in data.items() if value == max_el}

# def dict_to_list(data:dict)->tuple:
#     data_x = []
#     data_y = []
#     for key, value in data.items():
#         for y in range(value):
#             data_x.append(key)
#             data_y.append(y+1)
#     return data_x, data_y

# def average_fu(data:list)->float:
#     return round(sum(data) / len(data), 3)

# def median(data:list)->float:
#     loc_data = sorted(data)
#     n = len(loc_data)
#     if n % 2 == 0:
#         return (loc_data[n // 2] + loc_data[n // 2+1]) / 2
#     return loc_data[n // 2]


# inp = '2 1 3 4 2 4 2 5 3 2 6 1 0 7 2 1 3 2'
# data = list(map(int,inp.split()))

# data_x, data_y = dict_to_list(find_cnt(data))
# data_x_mode, data_y_mode = dict_to_list(mode(find_cnt(data)))

# plt.scatter(data_x, data_y)
# plt.scatter(data_x_mode,data_y_mode, color='red')
# plt.axvline(x=average_fu(data), color='orange')
# plt.axvline(x=median(data), color='green')
# plt.show()



import pandas as pd

stores = pd.read_csv(r'web\272\2\stores.csv')

print(stores)