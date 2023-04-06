import sqlite3 as sql

# 2 варианта подключения к базе данных
conn = sql.connect(r'bd\les1_272.db')
# conn = sql.connect(':memory:')

# это курсор, он обязателен для работы с sqlite
cur = conn.cursor()


cur.execute('SELECT * FROM users;')
# fetchhone - отвечает за вывод первой строчки при любом запросе
# one_result = cur.fetchone()
# print(one_result)


# fetchmany - отвечает за вывод определённого количества записей
# three_results = cur.fetchmany(3)
# print(three_results)


# fetchall - отвечает за вывод всех записей по запросу
all_results = cur.fetchall()
print(all_results)
conn.commit()
