# import random
# import statistics
# random.seed(100)
# n = 1000
# d = [random.randint(0,30) for i in range(n)]
# print(d)
# sr_ar = statistics.mean(d)
# print("Среднее арифметическое - " ,sr_ar)
# med = statistics.median(d)
# print("Медиана - ", med)
# moda = statistics.mode(d)
# print("мода - " ,moda)

# import random
# n = int(input('n = '))
# m = int(input('m = '))
# list1 = []
# list2 = []
# for i in range(m):
#     list1.append(random.randint(0, 1000))
# for i in range(n):
#     list2.append(list1[i : :n])
# print('получившиеся числа',  * list2)
# for i in range(len(list2)):
#     if len(list2[i]) % 2 == 0:
#         x = (sorted(list2[i])[len(list2[i])//2] + sorted(list2[i]) [(len(list2[i])//2)-1])/2
#     else: x = sorted(list2[i]) [len(list2[i])//2]
#     z = sum(list2[i])/len(list2[i])
#     print (f'{i+1} Мода: {list2[i]} / Медиана: {x} / Ср. значение{z}')


# import random
# random.seed(100)
# n = 1000
# d = [random.randint(0, 30) for i in range(n)]
# sr = sum(d) / len(d)

# range1 = max(d) - min(d)
# variance = 0
# for i in range(len(d)):
#     variance  += (d[i] - sr) ** 2
# variance = variance / len(d)
# print(range1, variance)

# import random
# import statistics
# random.seed(100)
# n = 1000
# d = [random.randint(0,30) for i in range(n)]
# kv_1 = statistics.median(d[0:500])
# print("1 квартиль: ", kv_1)
# median = statistics.median(d)
# kv_2 = median
# print("2 квартиль: ", kv_2)
# kv_3 = statistics.median(d[501:1000])
# print("3 квартиль: ", kv_3)


from random import randint


def data_generate(min_num, max_num, n):
    """
    генерация данных
    """
    data = [randint(min_num, max_num) for i in range(n)]
    return data


def average_fu(data):
    """
    среднее значение
    """
    return round(sum(data)/len(data), 3)


def sigma(data):
    """
    сигма
    """
    summa = 0
    av = average_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/len(data))**0.5, 3)


def z_scores(data):
    """
    z-преобразование
    """
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

# дописать квартили