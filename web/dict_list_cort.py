# словарик
# варианты объявления через фигурные скобки и через функцию dict{}
# mydict = {'j': "1", 'f': "2", 'm': "3"}
# print(mydict)
# mydict.

# вывод значения по ключу
# z = mydict['m']
# print(z)

# удаление по классике через del
# del mydict
# print(mydict)

# проверка на наличие ключа в словаре
# if 'j' in mydict:
#     print('ключ есть')
# else:
#     print('такого ключа нет')

# сортировка по ключу
# what_dict = {'b': 5, 'a': 8, 'y': -9, 'l': 0, 'd': 3}
# for key in sorted(what_dict):
#     print(key)

# сортировка по значению
# for key, val in sorted(what_dict.items(), key = lambda x: x[1]):
#     print(val)
# в этом случае возращается отсортированный список кортежей, а не словарь, но способ имеет место быть

# а это более правильный вариант
# element_sorted = {k: what_dict[k] for k in sorted(what_dict, key=what_dict.get, reverse= True)}
# print(element_sorted)

# перебор по ключам через .values() один из возможных вариантов
# iter_dict = {'key_c': 8, 'key_a': 1, 'key_k': -46, 'key_b': 80}
# for v in iter_dict.values():
#     print(v)

# объединение словарей по сути невозможно, но есть вариант добавить один словарь в другой
# what_dict = {'z':5, 't':8, 'x':-9, 'w':0, 'e':3}
# what_dict1 = {'b':900, 'a':48, 'y':-90, 'l':10, 'd':35}
# what_dict.update(what_dict1)
# print(what_dict)

#############################################################################################################
# список
# list1 =[9,5,9,7,1]
# print(list1)
# x = list1
# x = sorted(x, reverse=True)
# print('сортированный массив в реверсе', x)
# list1.sort()
# print(list1)

# вывод среза списка
# print(list1[1:3])

# вариант заполнения списка через ввод с клавиатуры
# mas = []
# for i in range(5): #ввод 5 элементов в цикле
#     mas.append(int(input())) #добавление целого числа, введенного с клавиатуры, в конец списка
# print(mas)

# заполнение списка через рандом
# import random #подключение модуля случайных чисел random
# mas=[] #объявление пустого списка
# for i in range(10):
#     mas.append(random.randint(0, 100)) #заполнение списка 10-ю случайными числами в диапазоне от 0 до 100
# print(mas) #вывод списка


#############################################################################################################
# #кортеж
# cort = (5,8,9,6,18,1)
# print("кортеж: ", cort)
# x = cort
# x = sorted(x)
# print("пример сортировки кортежа", x)
# cort1 = tuple("hello world this cort")
# print(cort1)
# # нумерация в кортежах с нуля
# print(cort[4])

# #удаление кортежа и не только его,  del можно применять к любым переменным
# del cort1
# print(cort1)

# пример вывода со срезом
# print(cort[start:finish:step]) #пример синтаксиса
# print(cort1.index('l'))

# сколько раз встречается элемент в кортеже
# print(cort1.count('l'))

# так же возможны преобразования кортежей в списки\словари(тут сложнее)\строки
# преобразование в строку
# game_name = ('Bob', ' ', 'liked', ' ', 'played', ' ', 'comp', ' ', 'games')
# print(type(game_name))
# game_name = ''.join(game_name)
# print(type(game_name))
# print(game_name)

# преобразование в список
# list_cort = (1, 5, 9, 0)
# print(list_cort)
# list_cort = list(list_cort)
# print(list_cort)

# преобразование в словарь
# score = (('bob', 8900), ('petya', 999000))
# print(score)
# score_dict = dict((x,y) for x, y in score)
# print(score_dict)


# именованные кортежи. в них можно присваивать значениям кортежа определённые индексы и к ним обращаться
from collections import namedtuple #сначала нужно импортировать namedtuple, чтобы работать с этим
citizen = namedtuple("Citizen", "name age status")
Alex = citizen(name='Alex Merc', age=27, status='show businessman')
# print(Alex.name, Alex.age, Alex.status)
print(Alex.name)
print(Alex.age)
print(Alex.status)
