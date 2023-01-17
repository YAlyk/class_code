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

import matplotlib.pyplot as plt
import numpy as np

flg = plt.figure()
ax = flg.add_subplot(111)

flg.set_facecolor('blue')
ax.set(facecolor='red')
plt.show()
