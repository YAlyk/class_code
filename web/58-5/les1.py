# import statistics as st
# from random import randint
# n = 1000
# data = [randint(0, 30) for el in range(n)]

# data_max = max(data)
# data_min = min(data)
# print('размах:', data_max-data_min)

# summa = 0
# av = st.mean(data)
# for el in data:
#     summa += (el-av)**2
# print('дисперсия', round(summa/len(data), 3))

# print(st.mean(data)) # среднее значение
# print(st.median(data)) # медиана
# print(st.mode(data)) # мода

from random import randint


def data_generate(min_num, max_num, n):
    data = [randint(min_num, max_num) for el in range(n)]
    return data


def average_fu(data):
    return round(sum(data)/len(data), 3)


def sigma(data):
    summa = 0
    av = average_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/len(data))**0.5, 3)


def z_scores(data):
    av = average_fu(data)
    sig = sigma(data)
    loc_data = []
    for el in data:
        loc_data.append(round((el-av)/sig, 3))
    return loc_data


data = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
data_2 = z_scores(data)

print('До стандартизации')
print('Данные:', data)
print('Среднее:', average_fu(data))
print('Стандартное отклонение', sigma(data))

print('После стандартизации')
print('Данные:', data_2)
print('Среднее:', average_fu(data_2))
print('Стандартное отклонение', sigma(data_2))
