# import pandas as pd
# # my_series = pd.Series([5, 6, 7, 8, 9, 10], index=[
# #                       'a', 'b', 'c', 'd', 'e', 'f'])
# # print(my_series[['a', 'b', 'f']])
# # print(my_series.index)
# # print(my_series.values)
# df = pd.DataFrame({'coutry': [
#                   'Kazahstan', 'Russia', 'Belarus', 'Ukraine'], 'population': [17.04, 143.5, 9.5, 4.5], 'square': [2724902, 17125191, 2017600, 603628]})
# df.index = ['KZ', 'RU', 'BY', 'UA']
# df.index.name='Country code'

# # print(df.loc['KZ'])

# # df.to_csv('coutry.csv', sep=',')
# print(df)


n = int(input())


def F_2(n):
 F_2 = []
 for x in range(1, n+1):
   if x % 2 == 0:
    F = 2 * x
    F_2.append(F)
    return F_2


print(F_2(n))
