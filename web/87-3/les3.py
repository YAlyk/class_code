# def sl_vich(a, b):
#    summ = a + b
#    vichit = a - b
#    print(summ, vichit)
#    return summ, vichit

# a = int(input("Введите первое число: "))
# b = int(input('Введите второе число: '))

# print(sl_vich(a, b))

# b = (2, 8, 9, 9, 9)
# c = True
# a = ['текст', "ещё текст"]
# print(b.count(9))

# print(type(a), type(c), type(b))

# a = bool(0) # a = False
# print(a)

# a =input('Введите оценки: ').split()
# print(sum(map(int,a)))

# ocenki = input('Введите оценки: ')
# #        start stop step
# print(ocenki[::5])


# ocenki = input('Введите оценки: ').split()
# one = ocenki[0:len(ocenki)//2]
# two = ocenki[len(ocenki)//2::]

# sr_one = sum(map(int, one))/len(one)
# sr_two = sum(map(int, two))/len(two)

# print("средняя оценка за первое полугодие:", sr_one,
#       '\t', 'Средняя оценка за второе полугодие:', sr_two)


a = input().split()
for i in a:
    print('*' * int(i))
