# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# plt.plot(x, y, 'g--')
# plt.title('График прямой')
# plt.xlabel('ось х')
# plt.ylabel('ось y')

# plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3

conn = sqlite3.connect('school.db')

# line
# plt.plot([2, 3, 4, 5])
# plt.title('Hey, bro!')
# plt.ylabel('Ось y')
# plt.xlabel('Ось x')
# plt.show()


# graphics
# x = [1,2,3, 4, 5, 6]
# y = [i**2 for i in x]
# plt.plot(x,y)
# plt.show()


# plt.plot([0, 1, 2, 3], [0, 3, 1, 2], [3, 1, 6, 4])
# plt.show()

# data = [2, 3, 4, 5]
# plt.plot(data, color = 'g')
# plt.plot(data, '--')
# plt.plot(data, '*')
# plt.plot(data, 'g*')
# plt.text(0, 4.5, 'Очень важный комментарий', family="verdana")
# plt.text(1, 2.5, 'Еще один очень важный комментарий', family="verdana")
# plt.show()


# data = [2, 3, 4, 5]
# plt.plot(data, 'r--')
# plt.savefig('saved_plot.png')
# plt.show()


table = pd.read_sql("SELECT * FROM students", conn)
table.info()
print(table)
print('___________________________')
print(table.head(5))

# sns.pairplot(table)
# sns.pairplot(table, hue='gender')

print(table['gender'].value_counts())
sns.countplot(x='gender', data=table)

# sns.countplot(x='id_classes', data=table, hue='gender')

# sns.violinplot(x='age', y='id_classes', data=table)
# sns.distplot(table['age'], kde=False)
# sns.distplot(table['age'])
# sns.kdeplot(table['age'], shade=True)

plt.show()


# Exercise
# table = pd.read_sql("SELECT * FROM students", conn)
# sns.countplot(x='age', data=table)

# table = pd.read_sql("SELECT * FROM classes", conn)
# sns.pairplot(table)

# table = pd.read_sql("SELECT * FROM marks", conn)
# print(table.head())
# sns.countplot('id_students', data=table, hue='mark')

# plt.show()


# Testing
# table.id_classes = table.id_classes.astype("int32")
# table.age = table.age.astype("int32")
# print(table.age.dtype)
