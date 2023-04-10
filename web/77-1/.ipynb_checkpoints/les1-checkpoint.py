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

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch',
           '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

# cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
# conn.commit()

# sql = """
# UPDATE albums
# SET artist = 'John Doe'
# WHERE artist = 'Andy Hunter'
# """
# cursor.execute(sql)
# conn.commit()

sql = "DELETE FROM albums WHERE artist = 'John Doe'"
cursor.execute(sql)
conn.commit()