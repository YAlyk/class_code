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

cur.execute("CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, "
             "familia CHAR, imya CHAR, otchestvo CHAR, id_classes INT NOT NULL, age INT(2), gender CHAR, "
             "FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)")

cur.execute("CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, "
             "mark INT, id_students INT NOT NULL, id_subjects INT NOT NULL, "
             "FOREIGN KEY (id_students) REFERENCES students (id) ON UPDATE CASCADE,"
             "FOREIGN KEY (id_subjects) REFERENCES subjects (id) ON UPDATE CASCADE)")

cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, "
             "subject CHAR)")
conn.commit()
