# def task (a:list, sum:int)->tuple:
#     stack = set()
#     for i in a:
#         if i not in stack:
#             stack.add(sum-i)
#         else:
#             return i, sum-i

# a = [-10, -1, 3, 5, 7, 23, 24]

# print(task(a,12))


# a = 'aabaa' # a = 60  b = 15
# b = 'aabaaa' # a = 75  b = 15
# c = 'aaaabbbbaabaaa' # a = 75   b = 15

# print(a[-1])


def read_csv(filename):
    data = {}
    with open(filename, 'r') as file:
        columns = tuple(file.readline().replace('\n', '').split(','))[1:]
        # print(columns)
        data = {i: [] for i in columns}
        for line in file:
            line = line.split(',')[1:]
            for col, value in zip(columns, line):
                #print(col, value)
                value = value.replace('\n', '')
                value = int(value) if value.isdigit() else value
                data[col].append(value)
    return data


# def print_data(data: dict):
#     columns = list(data.keys())
#     m = max([len(i) for i in columns])
#     for col in columns:
#         m = max(max(map(lambda x: len(str(x)), data[col])), m)
#     for i in columns:
#         print(str(i).ljust(m+1, ' '), end='')
#     print()
#     for i in range(len(data[list(data.keys())[0]])):
#         for col in columns:
#             print(str(data[col][i]).ljust(m+1, ' '), end='')
#         print()


# d= {'name': ['Max', 'Anna', 'Inna'], 'age': [13, 15, 25], 'group': ['IT', 'IT', 'ROBO']}

# print(read_csv('stores.csv'))
def size(data: dict):
    return len(data['name'])


def task_1(data: dict):
    for i in range(size(data)):
        if data['name'][i] == 'Hungary':
            return data['population'][i]


def task_2(data: dict):
    for i in range(size(data)):
        if data['name'][i] == 'Honduras':
            return data['area'][i]


def task_3(data: dict):
    areas = list(sorted(data['area'], reverse=True))[:10]
    for m in areas:
        for i in range(size(data)):
            if data['area'][i] == m:
                print(data['name'][i], m)


data = read_csv(r'web\71-1\71-1-3\countries.csv')
# print(data)
print('первый вопрос:', task_1(data))
print('второй вопрос:', task_2(data))
print('третий вопрос:')
task_3(data)
