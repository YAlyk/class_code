# 2 модуль


# def privetsctvie(a):
#     b = a ** 2
#     return b


# a = int(input())
# if a == 5:
#     print(privetsctvie(a))
# else:
#     pass


import sqlite3 as sql

# 2 варианта подключения к базе данных
conn = sql.connect(r'bd\les1_272.db')
# conn = sql.connect(':memory:')

# это курсор, он обязателен для работы с sqlite
cur = conn.cursor()

# cur.execute('тут пишем sql запрос')
cur.execute(""" CREATE TABLE IF NOT EXISTS users(
userid INT PRIMARY KEY,
fname TEXT,
lname TEXT,
gender TEXT);
""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
orderid INT PRIMARY KEY,
date TEXT,
userid TEXT,
total TEXT);
""")
conn.commit()

# cur.execute("""INSERT INTO users(
#     userid, 
#     fname, 
#     lname, 
#     gender)
#     VALUES(
#     '00001',
#     'Alex',
#     'Smith',
#     'male');
# """)

# conn.commit()

# user = ('00002', 'Lois', 'Lane', 'Female')

more_users = [('00003', 'Pater', 'Parker', 'male', '20'), ('00004', 'Bruce', 'Wayne', 'male', '30')]
# cur.execute("INSERT INTO users VALUES (?,?,?,?);", user)
# conn.commit()

cur.executemany('INSERT INTO users VALUES(?,?,?,?,?);', more_users)
conn.commit()


# cur.execute('DELETE FROM users WHERE userid = 2;')
# conn.commit()

# cur.execute('ALTER TABLE users ADD COLUMN age INTEGER DEFAULT 0;')
# conn.commit()
