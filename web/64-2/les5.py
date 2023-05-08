# print(0.10 + 0.10 + 0.10 + 0.10 + 0.10 + 0.10 + 0.10 + 0.10 + 0.10 + 0.10)
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)
plt.gray()
plt.matshow(digits.images[8])
plt.show()
