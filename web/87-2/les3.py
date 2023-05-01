import matplotlib.pyplot as plt


def get_data_from_file() -> tuple:
    file = open(r'web\87-2\lesson_4.txt', 'r')
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


def median(data: list) -> float:
    data.sort()
    if len(data) % 2 == 1:
        return data[len(data)//2]
    else:
        return (data[len(data)//2] + data[len(data)//2 - 1]) / 2

def kvartil_25(data:list)->float:
    loc_data=sorted(data)
    return median(loc_data[:len(loc_data)//2])


def kvartil_75(data: list) -> float:
    loc_data = sorted(data)
    return median(loc_data[len(loc_data)//2+1:])

def average_fu(data: list) -> float:
    return round(sum(data)/len(data), 3)


def sigma(data) -> int:
    summa = 0
    av = average_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/(len(data)-1))**0.5, 3)


def find_cnt(data: list) -> dict:
    dic = {}
    for el in set(data):
        dic[el] = data.count(el)

    return dic


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


m_h, m_w, f_h, f_w = get_data_from_file()


print('правило трёх сигм')
print('рост мужчины', percent_sigma(m_h))
print('вес мужчины', percent_sigma(m_w))
print('рост женщины', percent_sigma(f_h))
print('вес женщины', percent_sigma(f_w))
print('__________________________')
print('Статистика по мужчинам. Два числа - сначала для роста, потом для веса')
print('среднее значение', average_fu(m_h), average_fu(m_w))
print('стандартное отклонение', sigma(m_h), sigma(m_w))
print('минимальное значение', min(m_h), min(m_w))
print('максимальное значение', max(m_h), max(m_w))
print('первый квартиль', kvartil_25(m_h), kvartil_75(m_w))
print('медиана', median(m_h), median(m_w))
print('третий квартиль', kvartil_75(m_h), kvartil_75(m_w))
fig, axes = plt.subplots(2, 2)
x_m_h, y_m_h = data_to_bar(m_h)
x_m_w, y_m_w = data_to_bar(m_w)
x_f_h, y_f_h = data_to_bar(f_h)
x_f_w, y_f_w = data_to_bar(f_w)

axes[0, 0].bar(x_m_h, y_m_h, color='blue')
axes[0, 1].bar(x_m_w, y_m_w, color='red')
axes[1, 0].bar(x_f_h, y_f_h, color='blue')
axes[1, 1].bar(x_f_w, y_f_w, color='red')
plt.show()

