def sum_range(start, end):
    summa = 0
    for i in range(start, end+1):
        summa+=i
    print('сумма =', summa)

start_1 = int(input('Введите первое число: '))
end_1 = int(input('введите второе число: '))

if start_1 < end_1:
    sum_range(start_1, end_1)
elif start_1 > end_1:
    sum_range(end_1, start_1)
else:
    print(start_1)



x = int(input('введите высоту треугольника: '))
for i in range(x):
    print('%s%s' % (' ' * (x - i - 1), '^'  * (i*2+1)))
