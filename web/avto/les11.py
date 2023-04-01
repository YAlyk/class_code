# import sqlite3

# conn = sqlite3.connect('school.db')
# cur = conn.cursor()

# # Чтобы данные не добавлялись повторно при запуске программы
# cur.execute("DROP TABLE IF EXISTS classes")
# cur.execute("DROP TABLE IF EXISTS students")
# cur.execute("DROP TABLE IF EXISTS marks")
# cur.execute("DROP TABLE IF EXISTS subjects")

# cur.execute("PRAGMA foreign_keys=on")

# # Создание таблиц
# cur.execute("CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, "
#             "class CHAR(3), num_of_stud INT(2), teacher CHAR)")

# cur.execute("CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, "
#              "familia CHAR, imya CHAR, otchestvo CHAR, id_classes INT NOT NULL, age INT(2), gender CHAR, "
#              "FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)")

# cur.execute("CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, "
#              "mark INT, id_students INT NOT NULL, id_subjects INT NOT NULL, "
#              "FOREIGN KEY (id_students) REFERENCES students (id) ON UPDATE CASCADE,"
#              "FOREIGN KEY (id_subjects) REFERENCES subjects (id) ON UPDATE CASCADE)")

# cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, "
#              "subject CHAR)")
# conn.commit()


import sqlite3

conn = sqlite3.connect('school.db')
cur = conn.cursor()

# Чтобы данные не добавлялись повторно при запуске программы
cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS marks")
cur.execute("DROP TABLE IF EXISTS subjects")

cur.execute("PRAGMA foreign_keys=on")

# Создание таблиц
cur.execute("CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, "
            "class CHAR(3), num_of_stud INT(2), teacher CHAR)")

cur. execute("CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, "
             "familia CHAR, imya CHAR, otchestvo CHAR, id_classes INT NOT NULL, age INT(2), gender CHAR, "
             "FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)")

cur. execute("CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, "
             "mark INT, id_students INT NOT NULL, id_subjects INT NOT NULL, "
             "FOREIGN KEY (id_students) REFERENCES students (id) ON UPDATE CASCADE,"
             "FOREIGN KEY (id_subjects) REFERENCES subjects (id) ON UPDATE CASCADE)")

cur. execute("CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, "
             "subject CHAR)")


# Вставка данных
classes = ((1, "5A", 25, "Сергеева Наталья Петровна"),
           (2, "6A", 20, "Морозов Виталий Борисович"),
           (3, "10Б", 27, "Сидорова Ирина Вячеславовна"))
for i in classes:
    cur.execute("INSERT INTO classes VALUES(?, ?, ?, ?)", i)

students = ((1, "Иванов", "Иван", "Иванович", 2, 15, 'male'),
            (2, "Семенов", "Сергей", "Петрович", 1, 14, 'male'),
            (3, "Витолкина", "Светлана", "Эдуардовна", 2, 13, 'female'),
            (4, "Иванов", "Сергей", "Степанович", 3, 16, 'male'),
            (5, "Гусева", "Екатерина", "Павловна", 2, 14, 'female'),
            (6, "Павлова", "Оксана", "Геннадевна", 3, 16, 'female'),
            (7, "Игнатьев", "Игорь", "Дмитриевич", 1, 11, 'male'))
for i in students:
    cur.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?)", i)

subjects = ((1, "Python"),
            (2, "Mathematics"),
            (3, "History"))
for i in subjects:
    cur.execute("INSERT INTO subjects VALUES (?, ?)", i)

marks = ((1, 5, 1, 2),
         (2, 4, 2, 2),
         (3, 5, 2, 1),
         (4, 5, 1, 3),
         (5, 4, 1, 3))
for i in marks:
    cur.execute("INSERT INTO marks VALUES (?, ?, ?, ?)", i)

# Пробуем обновить ключ в родительской таблице и видим, что он поменялся и в дочерней таблице
# cur.execute("UPDATE classes SET id = 5 WHERE id = 1")

# Пробуем задать несуществующий внешний ключ
# cur.execute("UPDATE students SET id_classes = 33 WHERE id = 1")

# # Выборка данных
cur.execute("SELECT * FROM classes")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM subjects")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM marks")
rows = cur.fetchall()
print(rows)
# for row in rows:
#     print(row)

conn.commit()
conn.close()
