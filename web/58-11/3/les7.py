import pandas as pd
import matplotlib.pyplot as plt

stores = pd.read_csv('stores.csv')
stores.Size.hist()
plt.show()
