# sp = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
#       'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
#       'o': '---', 'p':
#           '.--.', 'q': '--.-',
#       'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
#       'y': '-.--', 'z': '--..',
#       '.': '.', '-': '-', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#       '5': '.....',
#       '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
# text = input().lower().split()
# arr = []
# for i in text:
#     for j in i:
#         print(sp[j], end=" ")
#     print()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# flight_data = sns.load_dataset('flights')
# # print(flight_data.head())
# sns.scatterplot(data=flight_data, x='year', y='passengers')
# sns.lineplot(data=flight_data, x='year', y='passengers')
# sns.barplot(data=flight_data, x='year', y='passengers')


# dimonds_data = sns.load_dataset('diamonds')
# plt.subplot(1, 2, 1)
# sns.countplot(x = 'carat', data=dimonds_data)
# plt.subplot(1, 2, 2)
# sns.countplot(x='depth', data=dimonds_data)

# drinks_df = pd.read_csv("web/24-H/drinks.csv")
# sns.barplot(x="country", y="beer_servings", data=drinks_df)

# maps_df = pd.read_csv("web/24-H/OldMaps.csv")
# sns.lineplot(x="name", y="year", data=maps_df)
# # print(maps_df.head())
# plt.show()
