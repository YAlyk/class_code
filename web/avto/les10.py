import sqlite3

conn = sqlite3.connect('mydatabase.db')
cur = conn.cursor()

# queru = 'CREATE TABLE IF NOT EXISTS book(author TEXT, year INT)'
# cur.execute(queru)
# cur.execute('INSERT INTO book VALUES("Pushkin", 1799)')

# book1 = ('Esenin', 1890)
# cur.execute('INSERT INTO book VALUES(?, ?)', book1)


# cur.execute('UPDATE book SET year=1895 WHERE author="Esenin"')

# cur.execute('SELECT * FROM book WHERE year=1799')
# cur.execute('SELECT author, year FROM book')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()