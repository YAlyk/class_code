import matplotlib.pyplot as plt
import random
from collections import Counter


# def data_generate():
#     random.seed(100)
#     data = [random.randint(0, 30) for el in range(1000)]

#     return data


def averge_fu(data):
    return round(sum(data)/len(data), 3)


# def mode(data):
#     c = Counter(data)
#     return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


# def median(data):
#     n = len(data)
#     index = n // 2
#     if n % 2:
#         return sorted(data)[index]
#     else:
#         return sum(sorted(data)[index-1:index+1]) / 2


def sigma(data):
    summa = 0
    av = averge_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/len(data)-1) ** 0.5, 3)


# def rang(data):
#     mi = min(data)
#     ma = max(data)
#     return ma-mi


# def z_score(data):
#     av = averge_fu(data)
#     sig = sigma(data)
#     print(av, sig)

#     loc_data = []
#     for el in data:
#         loc_data.append(round((el - av) / sig, 3))
#     return loc_data

#     # тернарная операция

#     # a if <условие> else b
#     # if <условие>:
#     #     d = a
#     # else:
#     #     d = b
# data = data_generate()
# data2 = z_score(data)

# print('до стандартизации')
# print('среднее значение:', averge_fu(data))
# print('мода:', mode(data))
# print('медиана:', median(data))
# print('среднеквадратичное отклонение:', sigma(data))
# print('размах:', rang(data))
# print()
# print('после стандартизации')
# print('среднее значение:', averge_fu(data2))
# print('мода:', mode(data2))
# print('медиана:', median(data2))
# print('среднеквадратичное отклонение:', sigma(data2))
# print('размах:', rang(data2))


# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 2, 4, 6, 8, 10, 12]

# plt.plot(x, y, color='red')


# def y(x: float) -> float:
#     return x ** 2


# x_min = -10.0
# x_max = 10.0
# data_x = [x for x in range(x_min, x_max+1, 0.5)]
# data_y = list(map(y, data_x))
# plt.scatter(data_x, data_y)

# def find_cnt(data: list) -> dict:
#     dic = {}
#     for el in set(data):
#         dic[el] = data.count(el)
#     return dic


# def mode(data: dict) -> dict:
#     max_el = max(data.values())
#     a = {}
#     # for key, value in data.items:
#     #     if value == max_el:
#     #         a[key] =value
#     return {key: value for key, value in data.items() if value == max_el}


# def dict_to_list(data: dict) -> tuple:
#     data_x = []
#     data_y = []
#     for key, value in data.items():
#         for y in range(value):
#             data_x.append(key)
#             data_y.append(y+1)
#     return data_x, data_y


# def average_fu(data: list) -> float:
#     return round(sum(data)/len(data), 3)


# def median(data: list) -> float:
#     loc_data = sorted(data)
#     n = len(data)
#     if n % 2 == 0:
#         return (loc_data[n//2] + loc_data[n//2 + 1]) / 2

#     return loc_data[n//2]


# inp = '2 1 3 4 2 4 2 5 3 2 6 1 0 7 2 1 3 2 6 6 6 6 6'  # можно инпут
# data = list(map(int, inp.split()))

# data_x, data_y = dict_to_list(find_cnt(data))
# data_x_mode, data_y_mode = dict_to_list(mode(find_cnt(data)))


# plt.scatter(data_x, data_y)
# plt.scatter(data_x_mode, data_y_mode, color='red')
# plt.axvline(x=average_fu(data), color='orange')
# plt.axvline(x=median(data), color='green')
# plt.show()


def find_cnt(data: list) -> dict:
    dic = {}
    for el in set(data):
        dic[el] = data.count(el)
    return dic


def mode(data: dict) -> dict:
    max_el = max(data.values())
    a = {}
    # for key, value in data.items:
    #     if value == max_el:
    #         a[key] =value
    return {key: value for key, value in data.items() if value == max_el}


def dict_to_list(data: dict) -> tuple:
    data_x = []
    data_y = []
    for key, value in data.items():
        for y in range(value):
            data_x.append(key)
            data_y.append(y+1)
    return data_x, data_y


def average_fu(data: list) -> float:
    return round(sum(data)/len(data), 3)


def median(data: list) -> float:
    loc_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (loc_data[n//2] + loc_data[n//2 + 1]) / 2

    return loc_data[n//2]


def get_data_from_file() -> tuple:
    file = open(r'web\64-2\lesson_4.txt', 'r')
    file = [line.strip() for line in file]

    male_height = []
    male_weight = []

    female_height = []
    female_weight = []

    non_height = []
    non_weight = []

    for line in file:
        q = line.split()
        sex, height, weight = q[0], int(q[1]), int(q[2])
        if sex == 'Male':
            male_height.append(height)
            male_weight.append(weight)
        else:
            female_height.append(height)
            female_weight.append(weight)

    return male_height, male_weight, female_height, female_weight


def data_to_bar(data: list) -> tuple:
    tup = find_cnt(data)
    x, y = [], []
    for el in tup:
        x.append(el)
        y.append(tup[el])

    return x, y


def percent_sigma(data):
    sig = sigma(data)
    av = average_fu(data)
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    n = len(data)
    for el in data:
        if abs(el-av) <= sig:  # |el| = abs(el)
            cnt_1 += 1
        if abs(el-av) <= 2 * sig:
            cnt_2 += 1
        if abs(el-av) <= 3 * sig:
            cnt_3 += 1
    return round(cnt_1/n*100, 3), round(cnt_2/n*100, 3), round(cnt_3/n*100, 3)



fig, axes = plt.subplots(2, 2)

m_h, m_w, f_h, f_w = get_data_from_file()
x_m_h, y_m_h = data_to_bar(m_h)
x_m_w, y_m_w = data_to_bar(m_w)
x_f_h, y_f_h = data_to_bar(f_h)
x_f_w, y_f_w = data_to_bar(f_h)

print('правило трёх сигм')
print('рост мужчины', percent_sigma(m_h))
print('вес мужчины', percent_sigma(m_w))
print('рост женщины', percent_sigma(f_h))
print('вес женщины', percent_sigma(f_w))


axes[0, 0].bar(x_m_h, y_m_h, color='red')
axes[0, 1].bar(x_m_w, y_m_w, color='blue')
axes[1, 0].bar(x_f_h, y_f_h, color='red')
axes[1, 1].bar(x_f_w, y_f_w, color='blue')
plt.show()
