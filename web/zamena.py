import pandas as pd
stores = pd.read_csv('stores.csv')

print(stores.describe())
print('__________________')
print(stores.dtypes())
print('__________________')
print(stores.shape())
print('__________________')
print(stores.size())
