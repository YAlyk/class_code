# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()
# # значения в скобках - кол-во строк, кол-во столбцов, индекс ячейки.
# ax_1 = fig.add_subplot(3, 1, 1)
# ax_2 = fig.add_subplot(3, 2, 4)
# ax_3 = fig.add_subplot(3, 3, 9)

# ax_1.set(title='ax_1', xticks=[], yticks=[])
# ax_2.set(title='ax_2', xticks=[], yticks=[])
# ax_3.set(title='ax_3', xticks=[], yticks=[])

# plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()

# ax_1 = fig.add_subplot(3, 1, 1)
# ax_2 = fig.add_subplot(6, 3, 3)
# ax_3 = fig.add_subplot(3, 3, 4)
# ax_4 = fig.add_subplot(3, 3, 6)
# ax_5 = fig.add_subplot(3, 4, 10)
# ax_6 = fig.add_subplot(5, 5, 25)

# ax_1.set(title='ax_1', xticks=[], yticks=[])
# ax_2.set(title='ax_2', xticks=[], yticks=[])
# ax_3.set(title='ax_3', xticks=[], yticks=[])
# ax_4.set(title='ax_4', xticks=[], yticks=[])
# ax_5.set(title='ax_5', xticks=[], yticks=[])
# ax_6.set(title='ax_6', xticks=[], yticks=[])

# plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# fig, axes = plt.subplots(nrows=2, ncols=2)
# axes[0, 0].set(title='axes[0][0]')
# axes[0, 1].set(title='axes[0][1]')
# axes[1, 0].set(title='axes[1][0]')
# axes[1, 1].set(title='axes[1][1]')

# for ax in axes.flat:
#     ax.set(xticks=[], yticks=[])
# print(plt.subplots(nrows=2, ncols=2))
# plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# ax.set(title='Axes')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# import pandas as pd

# fig, ax = plt.subplots()

# x = np.arange(0, 10, 0.1)
# y = np.sin(x)
# z = np.cos(x)

# ax.plot(y, color='blue', label='Sine wave')
# ax.plot(z, color='black', label='Cosine wave')

# leg = ax.legend(loc='best', frameon=False)
# plt.show()
