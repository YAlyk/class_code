import sqlite3

# NULL - значение NULL
# INTEGER - целые числа
# REAL - ЧИСЛА С ПЛАВАЮЩЕЙ ТОЧКОЙ
# TEXT - ТЕКС
# BLOB - БИНАРНЫЕ ЗНАЧЕНИЯ

conn = sqlite3.connect('les5.db')

cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
#    userid INT PRIMARY KEY,
#    fname TEXT,
#    lname TEXT,
#    gender TEXT);
# """)

# cur.execute("""CREATE TABLE IF NOT EXISTS orders(
#    orderid INT PRIMARY KEY,
#    date TEXT,
#    userid TEXT,
#    total TEXT);
# """)

# cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
#    VALUES('00001', 'Alex', 'Smith', 'male');""")
# user = ('00002', 'Lois', 'Lane', 'Female')
# more_users = [('00003', 'Peter', 'Parker', 'Male'),
#               ('00004', 'Bruce', 'Wayne', 'male')]
# cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)

# cur.execute("""CREATE TABLE user(
#    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
#    email TEXT,
#    paasw TEXT);
# """)
# cur.execute("""INSERT INTO user(email, paasw) 
#    VALUES('testmail@mail.ru', 'testpassword');""")


# cur.execute("""CREATE TABLE rubr(
#    id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
#    name_rubr TEXT);
# """)

# cur.execute("""CREATE TABLE site(
#    id_site INTEGER PRIMARY KEY AUTOINCREMENT,
#    id_user INTEGER,
#    id_rubr INTEGER,
#    url TEXT,
#    title TEXT,
#    msg TEXT);
# """)

# cur.execute("""DROP TABLE site""")

# cur.execute("""INSERT INTO user(email, paasw)
#    VALUES('testmail@mail.ru', 'testpassword');""")

# cur.execute("""INSERT INTO rubr VALUES(NULL, 'Программирование');""")

# cur.execute("""DELETE FROM site WHERE id_rubr=1; """)

# cur.execute("""INSERT INTO site(id_user, id_rubr, url, title, msg) VALUES(1,3,'http://wwwadmin.ru', 'Название', 'Описание');""")

conn.commit()
