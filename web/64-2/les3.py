import matplotlib.pyplot as plt
import random
from collections import Counter


def averge_fu(data):
    return round(sum(data)/len(data), 3)


def sigma(data):
    summa = 0
    av = averge_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/len(data)-1) ** 0.5, 3)


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


# def average_fu(data: list) -> float:
#     return round(sum(data)/len(data), 3)


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
    av = averge_fu(data)
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


def kvartil_25(data):
    loc_data = sorted(data)
    return median(loc_data[:len(loc_data)//2])


def kvartil_75(data):
    loc_data = sorted(data)
    return median(loc_data[len(loc_data)//2+1:])


def corr_coef(x, y):
    x_mid = averge_fu(x)
    y_mid = averge_fu(y)

    chisl = 0

    for i in range(len(x)):
        chisl += (x[i]-x_mid) * (y[i]-y_mid)
    return round(chisl / (sigma(x)*sigma(y) * (len(x)-1)), 3)


def get_coeff_k_b(data_x, data_y):
    sigma_x = sigma(data_x)
    sigma_y = sigma(data_y)
    r_xy = corr_coef(data_x, data_y)
    k = round((sigma_y/sigma_x)*r_xy, 3)
    b = round(averge_fu(data_y) - k * averge_fu(data_x), 3)
    return k, b


def get_line(data_x, data_y):
    k, b = get_coeff_k_b(data_x, data_y)
    x = []
    y = []
    x_min = min(data_x)
    x_max = max(data_x)

    x.append(x_min)
    y.append(k*x_min+b)

    x.append(x_max)
    y.append(k*x_max+b)

    return x, y, k, b


m_h, m_w, f_h, f_w = get_data_from_file()
x_m_h, y_m_h = data_to_bar(m_h)
x_m_w, y_m_w = data_to_bar(m_w)
x_f_h, y_f_h = data_to_bar(f_h)
x_f_w, y_f_w = data_to_bar(f_h)
m_l_x, m_l_y, m_k, m_b = get_line(m_w, m_h)
f_l_x, f_l_y, f_k, f_b = get_line(f_w, f_h)

print('правило трёх сигм')
print('рост мужчины', percent_sigma(m_h))
print('вес мужчины', percent_sigma(m_w))
print('рост женщины', percent_sigma(f_h))
print('вес женщины', percent_sigma(f_w))

print()
print('Статистика по мужчинам. Два числа - сначала для роста, потом для веса')
print('среднее значение', averge_fu(m_h), averge_fu(m_w))
print('стандартное отклонение', sigma(m_h), sigma(m_w))
print('минимальное значение', min(m_h), min(m_w))
print('первый квартиль', kvartil_25(m_h), kvartil_25(m_w))
print('медиана/2 квартиль', median(m_h), median(m_w))
print('третий квартиль', kvartil_75(m_h), kvartil_75(m_w))
print('максимальное значение', max(m_h), max(m_w))
print()
print('Статистика по женщинам. Два числа - сначала для роста, потом для веса')
print('среднее значение', averge_fu(f_h), averge_fu(f_w))
print('стандартное отклонение', sigma(f_h), sigma(f_w))
print('минимальное значение', min(f_h), min(f_w))
print('первый квартиль', kvartil_25(f_h), kvartil_25(f_w))
print('медиана/2 квартиль', median(f_h), median(f_w))
print('третий квартиль', kvartil_75(f_h), kvartil_75(f_w))
print('максимальное значение', max(f_h), max(f_w))

# fig, axes = plt.subplots(1, 2)

# print()
# print('коэффициент корреляции для мужчин', corr_coef(m_h, m_w))
# print('коэффициент корреляции для женщин', corr_coef(f_h, f_w))
# print('коэффициент детерминации для мужчин', round(corr_coef(m_h, m_w)**2, 3))
# print('коэффициент детерминации для женщин', round(corr_coef(f_h, f_w)**2, 3))
# axes[0].scatter(m_w, m_h, color='blue')
# axes[0].plot(m_l_x, m_l_y, color='red')
# axes[1].scatter(f_w, f_h, color='red')
# axes[1].plot(f_l_x,f_l_y, color='blue')

fig, axes = plt.subplots(2, 2)
axes[0, 0].bar(x_m_h, y_m_h, color='red')
axes[0, 1].bar(x_m_w, y_m_w, color='blue')
axes[1, 0].bar(x_f_h, y_f_h, color='red')
axes[1, 1].bar(x_f_w, y_f_w, color='blue')
plt.show()
