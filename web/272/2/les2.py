import sqlite3 as sql

# 2 варианта подключения к базе данных
conn = sql.connect(r'bd\les2_272.db')
# conn = sql.connect(':memory:')

# это курсор, он обязателен для работы с sqlite
cur = conn.cursor()


# cur.execute('SELECT * FROM users;')
# fetchhone - отвечает за вывод первой строчки при любом запросе
# one_result = cur.fetchone()
# print(one_result)


# fetchmany - отвечает за вывод определённого количества записей
# three_results = cur.fetchmany(3)
# print(three_results)


# fetchall - отвечает за вывод всех записей по запросу
# all_results = cur.fetchall()
# print(all_results)
# conn.commit()


# cur.execute(""" CREATE TABLE IF NOT EXISTS tmp3(
# id INT);
# """)
# conn.commit()

# cur.execute("""INSERT INTO tmp3(id) VALUES(1);""")
# cur.execute("""INSERT INTO tmp3(id) VALUES(2);""")
# cur.execute("""INSERT INTO tmp3(id) VALUES(3);""")
# cur.execute("""INSERT INTO tmp3(id) VALUES(4);""")
# cur.execute("""INSERT INTO tmp3(id) VALUES(5);""")
# conn.commit()

# cur.execute('DROP TABLE tmp3;')
# conn.commit()

# cur.execute('SELECT * FROM tmp3 LIMIT 3;')
# cur.execute('SELECT * FROM tmp3 LIMIT 2, 3;')
# cur.execute('SELECT * FROM tmp3 LIMIT 3 OFFSET 2;')

# cur.execute('SELECT "ы"="Ы", "ы"="Ы" COLLATE NOCASE')
# dan = cur.fetchall()
# print(dan)
# conn.commit()

cur.execute(""" CREATE TABLE IF NOT EXISTS departments(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR NOT NULL);
""")
conn.commit()

cur.execute("""INSERT INTO departments
([Id], [name])
VALUES
(1,'HR'),
(2,'Sales'),
(3, 'Tech')""")
conn.commit()
