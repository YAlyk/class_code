# import sqlite3

# conn = sqlite3.connect('les5.db')

# cursor = conn.cursor()

# # user = [(2, 'testmail2@mail.ru', 'password'), (3, 'testmail2@mail.ru', 'logpar')]
# # cursor.executemany("INSERT INTO user VALUES (?,?,?)", user)

# # rub = [(1, 'Робототехника'), (2, 'Биотехнологии')]
# # cursor.executemany("INSERT INTO rubr VALUES (?,?)", rub)


# # sit = [(3, 2, 2, 'https://www.bioteh.ru', 'Биотехнологии', 'сайт по биотеху'),
# #        (4, 3, 3, 'https://www.ROBO.ru', 'Робототехника', 'сайт по робототехнике')]
# # cursor.executemany("INSERT INTO site VALUES ( ?, ?, ?, ?, ?, ?)", sit)

# # cursor.execute('SELECT * FROM site;')
# # a = cursor.fetchmany(4)
# # print(a)

# # cursor.execute('SELECT * FROM site;')
# # a = cursor.fetchmany(1)
# # print(a)


# # cursor.execute('SELECT * FROM site;')
# # a = cursor.fetchone()
# # print(a)


# # cursor.execute('SELECT * FROM site;')
# # a = cursor.fetchall()
# # print(a)

# # a = cursor.execute(f"SELECT * FROM user WHERE id_user = 2;")
# # conn.commit()
# # a = a.fetchone()
# # print(a)

# conn.commit()


import sqlite3
db = sqlite3.connect('1.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS Employees (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FName VARCHAR NOT NULL,
    LName VARCHAR NOT NULL,
    PhoneNumber VARCHAR,
    ManagerId INTEGER REFERENCES Employees(Id),
    DepartmentId INTEGER REFERENCES departments(Id),
    Salary INT NOT NULL,
    HireDate DATETIME NOT NULL
);""")
db.commit()

sql.execute("""INSERT INTO Employees
    ([Id], [FName], [LName], [PhoneNumber], [ManagerId], [DepartmentId], [Salary], [HireDate])
VALUES
    (1, 'James', 'Smith', 1234567890, NULL, 1, 1000, '01-01-2002'),
    (2, 'John', 'Johnson', 2468101214, '1', 1, 400, '23-03-2005'),
    (3, 'Michael', 'Williams', 1357911131, '1', 2, 600, '12-05-2009'),
    (4, 'Johnathon', 'Smith', 1212121212, '2', 1, 500, '24-07-2016')""")
db.commit()
