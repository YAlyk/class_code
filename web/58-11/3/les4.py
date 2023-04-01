import matplotlib.pyplot as plt
import random

# Функции 2 урока

def data_generate(min_num, max_num, n):
    data = [random.randint(min_num, max_num) for el in range(n)]

    return data


def average(data):

    return round(sum(data) / len(data))


def sigma(data) -> int:
    summa = 0
    av = average_fu(data)

    for el in data:
        summa += (el - av) ** 2

    # По сравнение со 2 уроком исправлено округление и перевод в int
    return int(round((summa / (len(data) - 1)) ** 0.5, 0))


def z_scores(data):
    av = average_fu(data)
    sig = sigma(data)
    print(av, sig)

    loc_data = []
    for el in data:
        loc_data.append(round((el - av) / sig, 3))

    return loc_data

# Функции 3 урока


def find_cnt(data: list) -> dict:
    # Функция возвращает словарь, где ключ - число, значение - сколько раз
    # встречается число в наборе данных
    dic = {}

    for el in set(data):
        dic[el] = data.count(el)

    return dic


def mode(data: dict) -> dict:
    # Функция возвращает словарь с модами, где ключ - это само число
    # значение - сколько раз повторился ключ в исходном наборе данных
    max_el = max(data.values())

    return {key: value for key, value in data.items() if value == max_el}


def dict_to_list(data: dict) -> tuple:
    # На вход получает словарь и возвращает кортеж из двух списков (x, y)
    # где каждый key повторяется value раз
    # для построения графика

    data_x = []
    data_y = []

    for key, value in data.items():
        for y in range(value):
            data_x.append(key)
            data_y.append(y + 1)

    return data_x, data_y


def average_fu(data: list) -> float:
    # Среднее арифметическое
    return round(sum(data) / len(data), 3)


def median(data: list) -> float:
    loc_data = sorted(data)
    n = len(loc_data)
    if n % 2 == 0:
        return (loc_data[n // 2 - 1] + loc_data[n // 2]) / 2

    return loc_data[n // 2]


def kvartil_25(data):
    loc_data = sorted(data)
    return median(loc_data[:len(loc_data)//2])


def kvartil_75(data):
    loc_data = sorted(data)
    return median(loc_data[len(loc_data)//2 + 1:])

# Ниже функции 4 урока


def get_data_from_file() -> tuple:
    # Получаем 4 массива. По 2 массива с ростом и весом для мужчин и женщин

    file = open('C:/Users/koksh/Desktop/pyton/code/web/58-11/3/lesson_4.txt', 'r')

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
    '''
    На вход получаем список с данными типа int
    Возвращаем кортеж из двух списков, где первый список - характеристика (например, вес) - для оси иск
    Второй список - сколько раз эта характеристика встретилась в данных - для оси игрек
    '''
    tup = find_cnt(data)
    x, y = [], []
    for el in tup:
        x.append(el)
        y.append(tup[el])

    return x, y


def percent_sigma(data):
    sig = sigma(data)
    # print(sig)
    av = average(data)
    # print(av)
    cnt_1 = 0  # в пределах сигмы
    cnt_2 = 0  # в пределах двух сигм
    cnt_3 = 0  # в пределах трех сигм
    n = len(data)

    for el in data:
        # print(el)
        if abs(el - av) <= sig:
            cnt_1 += 1
        if abs(el - av) <= 2 * sig:
            cnt_2 += 1
        if abs(el - av) <= 3 * sig:
            cnt_3 += 1
    return round(cnt_1 / n * 100, 3), round(cnt_2 / n * 100, 3), round(cnt_3 / n * 100, 3)


m_h, m_w, f_h, f_w = get_data_from_file()

print('Статистика по мужчинам. Два числа - сначала для роста, потом для веса')
print(f'Среднее значение', average(m_h), average(m_w))
print(f'Стандартное отклонение', sigma(m_h), sigma(m_w))
print(f'Минимальное значение', min(m_h), min(m_w))
print(f'25 % (Первый квартиль)', kvartil_25(m_h), kvartil_25(m_w))
print(f'50 % (Медиана)', median(m_h), median(m_w))
print(f'75 % (Третий квартиль)', kvartil_75(m_h), kvartil_75(m_w))
print(f'Максимальное значение', max(m_h), max(m_w))
print('<------------------------->')
print('Статистика по женщинам. Два числа - сначала для роста, потом для веса')
print(f'Среднее значение', average(f_h), average(f_w))
print(f'Стандартное отклонение', sigma(f_h), sigma(f_w))
print(f'Минимальное значение', min(f_h), min(f_w))
print(f'25 % (Первый квартиль)', kvartil_25(f_h), kvartil_25(f_w))
print(f'50 % (Медиана)', median(f_h), median(f_w))
print(f'75 % (Третий квартиль)', kvartil_75(f_h), kvartil_75(f_w))
print(f'Максимальное значение', max(f_h), max(f_w))


print('Правило трех сигм')
print('Рост, мужчины', percent_sigma(m_h))
print('Вес, мужчины', percent_sigma(m_w))
print('Рост, женщины', percent_sigma(f_h))
print('Вес, женщины', percent_sigma(f_w))

# Строим графики

fig, axes = plt.subplots(2, 2,)


x_m_h, y_m_h = data_to_bar(m_h)
x_m_w, y_m_w = data_to_bar(m_w)
x_f_h, y_f_h = data_to_bar(f_h)
x_f_w, y_f_w = data_to_bar(f_w)

axes[0, 0].bar(x_m_h, y_m_h, color='red')
axes[0, 1].bar(x_m_w, y_m_w, color='blue')
axes[1, 0].bar(x_f_h, y_f_h, color='red')
axes[1, 1].bar(x_f_w, y_f_w, color='blue')
plt.show()
