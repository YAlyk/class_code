# import random
# random.seed(100)


# def data_generate():
#     n = 1000
#     data = [random.randint(0, 30) for i in range(n)]
#     return (data)


# def average_fu(data):
#     return round(sum(data)/len(data), 3)


# def sigma(data):
#     summa = 0
#     av = average_fu(data)
#     for el in data:
#         summa += (el-av)**2
#     return round((summa/(len(data)-1))**0.5, 3)


# def otk(data):
#     diffs = 0
#     avg = sum(data)/len(data)
#     for i in data:
#         diffs += (i-avg)**2
#     return (diffs/(len(data)))**0.5


# def raz(data):
#     m = max(data)
#     n = min(data)
#     return m - n


# def mean(data):
#     return sum(data) / len(data)


# def median(data):
#     data.sort()
#     if len(data) % 2 == 1:
#         return data[len(data)//2]
#     else:
#         return (data[len(data)//2] + data[len(data)//2 - 1]) / 2


# def mode(data):
#     d = dict()
#     for elem in data:
#         if elem in d.keys():
#             d[elem] += 1
#         else:
#             d[elem] = 1
#     mx = max(d.values())
#     res = []
#     for key in d.keys():
#         if d[key] == mx:
#             res.append(d[key])
#     return res


# def z_scores(data):
#     av = average_fu(data)
#     sig = sigma(data)
#     print(av, sig)

#     loc_data = []
#     for el in data:
#         loc_data.append(round((el - av) / sig, 3))

#     return loc_data


# data = data_generate()
# data2 = z_scores(data)

# print('до стандартизации')
# print('ср знач:', mean(data))
# print('мода:', mode(data))
# print('медиана', median(data))
# print('размах:', raz(data))
# print('среднеквадратичное отклонение:', otk(data))
# print()

# print('после стандартизации')
# print('ср знач:', mean(data2))
# print('мода:', mode(data2))
# print('медиана', median(data2))
# print('размах:', raz(data2))
# print('среднеквадратичное отклонение:', otk(data2))


import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 2]
# y = [1, 4, 9, 16, 25, 10]

# plt.scatter(x, y)
# x = [0, 1, 2, 3, 4, 5, 6, 7]
# y = [2, 1, 3, 4, 2, 4, 2, 5, 3, 2, 6, 1, 0, 7, 2, 1, 3, 2]
# plt.scatter([2, 1, 3, 4, 2, 4, 2, 5, 3, 2, 6, 1, 0, 7,
#          2, 1, 3, 2], color='#C44E52', marker='*')
# plt.show()


def find_cnt(data: list) -> dict:
    dic = {}
    for el in set(data):
        dic[el] = data.count(el)

    return dic


def mode(data: list) -> dict:
    max_el = max(data.values())
    return {key: value for key, value in data.items() if value == max_el}


def dict_to_list(data: list) -> tuple:
    data_x = []
    data_y = []

    for key, value in data.items():
        for y in range(value):
            data_x.append(key)
            data_y.append(y+1)

    return data_x, data_y


def average_fu(data: list) ->float:
    return round(sum(data)/len(data), 3)


inp = '2 1 3 4 2 4 2 5 3 2 6 1 0 7 2 1 3 2 6 6 6 6 6'  # можно добавить инпут
data = list(map(int, inp.split()))

data_x, data_y = dict_to_list(find_cnt(data))
data_x_mode, data_y_mode = dict_to_list(mode(find_cnt(data)))

plt.scatter(data_x, data_y)
plt.scatter(data_x_mode, data_y_mode, color='red')
plt.axvline(x = average_fu(data), color='orange')
# plt.axvline()
plt.show()
