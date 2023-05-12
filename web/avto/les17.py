# # import matplotlib.pyplot as plt


# # plt.show()


# import matplotlib.pyplot as plt
# x = [1, 2, 5, 10, 37]
# y = [1, 2, 3, 4, 5]
# fig = plt.figure()
# plt.plot(x, y, color='red')
# plt.grid()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Создаём экземпляр класса figure и добавляем к Figure область Axes
# fig, ax = plt.subplots()
# # Добавим заголовок графика
# ax.set_title('График функции')
# # Название оси X:
# ax.set_xlabel('x')
# # Название оси Y:
# ax.set_ylabel('y')
# # Начало и конец изменения значения X, разбитое на 100 точек
# x = np.linspace(-5, 5, 100) # X от -5 до 5
# # Построение прямой
# y = 1 / x
# # Вывод графика
# ax.plot(x, y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Создаём экземпляр класса figure и добавляем к Figure область Axes
# fig, ax = plt.subplots()
# # Добавим заголовок графика
# ax.set_title('График функции')
# # Название оси X:
# ax.set_xlabel('x')
# # Название оси Y:
# ax.set_ylabel('y')
# # Начало и конец изменения значения X, разбитое на 100 точек
# x = np.linspace(-5, 5, 100) # X от -5 до 5
# # Построение прямой
# y = np.exp(x)
# # Вывод графика
# ax.plot(x, y)
# plt.show()