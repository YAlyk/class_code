import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flights_data = sns.load_dataset('flights')
# print(flights_data.head())

# sns.scatterplot(data=flights_data, x='year', y='passengers')
# sns.lineplot(data=flights_data, x='year', y='passengers')
# sns.barplot(data=flights_data, x='year', y='passengers')
# dimonds_data = sns.load_dataset('diamonds')
# plt.subplot(1,2,1)
# sns.countplot(x='carat', data=dimonds_data)
# plt.subplot(1,2,2)
# sns.countplot(x='depth', data=dimonds_data)
# plt.show()


# drinks_df = pd.read_csv('web/103-2/drinks.csv')
# sns.barplot(x='country', y='beer_servings', data = drinks_df)
# sns.set_style('darkgrid')
# sns.lineplot(data=flights_data, x='year', y='passengers')

# sns.set_style('whitegrid')
# sns.lineplot(data=flights_data, x='year', y='passengers')

tips_df = sns.load_dataset('tips')
print(tips_df.head())
plt.show()
