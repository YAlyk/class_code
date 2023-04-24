import random
random.seed(100)


def data_generate():
    n = 1000
    data = [random.randint(0, 30) for i in range(n)]
    return (data)


def average_fu(data):
    return round(sum(data)/len(data), 3)


def sigma(data):
    summa = 0
    av = average_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/(len(data)-1))**0.5, 3)


def otk(data):
    diffs = 0
    avg = sum(data)/len(data)
    for i in data:
        diffs += (i-avg)**2
    return (diffs/(len(data)))**0.5


def raz(data):
    m = max(data)
    n = min(data)
    return m - n


def mean(data):
    return sum(data) / len(data)


def median(data):
    data.sort()
    if len(data) % 2 == 1:
        return data[len(data)//2]
    else:
        return (data[len(data)//2] + data[len(data)//2 - 1]) / 2


def mode(data):
    d = dict()
    for elem in data:
        if elem in d.keys():
            d[elem] += 1
        else:
            d[elem] = 1
    mx = max(d.values())
    res = []
    for key in d.keys():
        if d[key] == mx:
            res.append(d[key])
    return res


print('ср знач:', mean(data))
print('мода:', mode(data))
print('медиана', median(data))
print('размах:', raz(data))
print('среднеквадратичное отклонение:', otk(data))
