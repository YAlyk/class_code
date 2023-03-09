# f = lambda x: x * x
# print(type(f))


# def func(x):
#     return x**2

# a = [1, 5, 6]  # список list
# a = (8, 6, 3)  # кортеж tuple
# a = {8, 8, 9, 6, 2, 5, 88, 8}  # множество set
# a = {'a': 5, 'b': 10}  # словарик dict

# print(a)


import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
# cursor.execute("""CREATE TABLE albums
# (title text, artist text, release_date text, publisher text, media_type text)  """)

cursor.commit()