# import matplotlib.pyplot as plt
# import decimal
# import numpy as np

# xmin = -20
# xmax = 20
# dx = 0.1

# xlist = np.around(np.arange(xmin, xmax, dx), decimals=4)

# ylist = 1 / xlist

# plt.plot(xlist, ylist)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# fig = plt.figure()
# x = np.linspace(0, 10, 10)
# y = 4*x
# y1 = x**2

# plt.scatter(x, y, color='r', label='4*x')
# plt.plot(x, y1, color='b', label='x**2')

# plt.xlabel('x')
# plt.ylabel('y1 y2')
# plt.title('График зависимости:у1=4*х, у2=х**2')

# plt.minorticks_on()
# plt.grid(which='major',
#          color='k',
#          linewidth=1)
# plt.grid(which='minor',
#          color='k',
#          linestyle=':')
# plt.legend()

# plt.show()


import sqlite3

# NULL - значение NULL
# INTEGER - целые числа
# REAL - ЧИСЛА С ПЛАВАЮЩЕЙ ТОЧКОЙ
# TEXT - ТЕКС
# BLOB - БИНАРНЫЕ ЗНАЧЕНИЯ

conn = sqlite3.connect('les4.db')

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")

# cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
#    VALUES('00001', 'Alex', 'Smith', 'male');""")
user = ('00002', 'Lois', 'Lane', 'Female')
more_users = [('00003', 'Peter', 'Parker', 'Male'),
              ('00004', 'Bruce', 'Wayne', 'male')]
# cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()
