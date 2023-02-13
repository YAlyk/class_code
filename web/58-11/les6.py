# import sqlite3

# conn = sqlite3.connect('les6.db')
# cur = conn.cursor()

# # тут пишем весь код

# conn.commit()


global data, columns
columns = ('id', 'name', 'lastname', 'age', 'height', 'weight')
data = []


def read(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.split(', ')
            line = (int(line[0]), line[1], line[2], int(
                line[3]), int(line[4]), int(line[5]))
            if line not in data:
                data.append(line)


def write(filename):
    with open(filename, 'w') as file:
        for line in data:
            file.write(', '.join([str(i) for i in line])+'\n')


def add(line: str):
    line = line.split(', ')
    line = (int(line[0]), line[1], line[2], int(
        line[3]), int(line[4]), int(line[5]))
    if line not in data:
        data.append(line)


def remove(key, value):
    col = columns.index(key)
    # print(col)
    row = -1
    for i in range(len(data)):
        if data[i][col] == value:
            row = i
            break
    if row == -1:
        print('No matches found')
    else:
        data.pop(row)


def print_data():
    for line in data:
        print(', '.join([str(i) for i in line]))


read('C:/Users/koksh/Desktop/pyton/code/input.txt')
print_data()
remove('id', 1)
print_data()
write('C:/Users/koksh/Desktop/pyton/code/input.txt')
