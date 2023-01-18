# import matplotlib.pyplot  as plt
# import numpy as np
# x = np.linspace(0, 10, 50)
# y1 = x
# y2 = [i**2 for i in x]
# plt.title('Зависимости: y1 = x, y2 = x^2')
# plt.xlabel('x')
# plt.ylabel('y1, y2')
# plt.grid()
# plt.plot(x, y1, x, y2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 10, 50)
# y1 = x
# y2 = [i**2 for i in x]
# plt.figure(figsize=(9, 9))
# plt.subplot(2, 1, 1)
# plt.plot(x, y1)
# plt.title('Зависимости: y1 = x, y2 = x^2')
# plt.ylabel('y1', fontsize=14)
# plt.grid(True)
# plt.subplot(2, 1, 2)
# plt.plot(x, y2)
# plt.xlabel('x', fontsize=16)
# plt.ylabel('y2',fontsize=20)
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# flg = plt.figure()
# ax = flg.add_subplot(111)

# flg.set(facecolor = 'green')
# ax.set(facecolor = 'red')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# flg = plt.figure()
# ax = flg.add_subplot(111)

# flg.set_facecolor('blue')
# ax.set(facecolor='red')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('Основы анатомии matplotlib', color='white', size=20)
# fig.set_facecolor('green')
# ax.set_facecolor('gray')
# ax.set_xlim([-10, 10])
# ax.set_ylim([-2, 2])
# # ax.set_title('Основное название графика')
# ax.set_xlabel('ось абсцис (XAxis)')
# ax.set_ylabel('ось ординат (YAxis)')
# plt.show()


# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)

# fig.set(facecolor='green')
# ax.set(facecolor='red',
#        xlim=[-10, 10],
#        ylim=[-2, 2],
#        title='Основы анатомии matplotlib',
#        xlabel='ось абцис (XAxis)',
#        ylabel='ось ординат (YAxis)')

# plt.show()


# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19], color='red', linewidth=5)
# ax.scatter([0,1,2,3,4], [1,3,8,12,27], color='blue', marker='*')
# plt.show()

# import matplotlib.pyplot as plt
# plt.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19], color='red', linewidth=2)
# plt.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 27], color='blue', marker='*')

# plt.show()


# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax_1 = fig.add_subplot(2, 2, 1)
# ax_2 = fig.add_subplot(2, 2, 2)
# ax_3 = fig.add_subplot(2, 2, 3)
# ax_4 = fig.add_subplot(2, 2, 4)

# ax_1.set(title='ax_1', xticks=[], yticks=[])
# ax_2.set(title='ax_2', xticks=[], yticks=[])
# ax_3.set(title='ax_3', xticks=[], yticks=[])
# ax_4.set(title='ax_4', xticks=[], yticks=[])

# plt.show()


# import matplotlib.pyplot as plt

# fig = plt.figure()
# #        кол-во строк # стобцов # индекс # ячейки
# ax_1 = fig.add_subplot(2, 3, 1)
# ax_2 = fig.add_subplot(2, 3, 3)
# ax_3 = fig.add_subplot(2, 3, 5)

# ax_1.set(title='ax_1', xticks=[], yticks=[])
# ax_2.set(title='ax_2', xticks=[], yticks=[])
# ax_3.set(title='ax_3', xticks=[], yticks=[])

# plt.show()


