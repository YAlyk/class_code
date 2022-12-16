# one_otvet = input('первый вопрос: ')
# two_otvet = input('второй вопрос: ')

# if one_otvet == 'да' and two_otvet == 'да':
#     print('оба ответа да')
# elif one_otvet == 'да' and two_otvet == 'нет':
#     print('первый да, второй нет')
# elif one_otvet == 'нет' and two_otvet == 'да':
#     print('первый нет, второй да')
# elif one_otvet == 'нет' and two_otvet == 'нет':
#     print('оба ответа нет')
# else:
#     print('ошибка ввода, введены не те ответы')

while True:
    a=int(input('первое число: '))
    c=str(input('знак: '))
    b=int(input('второе число: '))
    if c=="*":
        print(a*b)
        break
    if c=="-":
        print(a-b)
        break
    if c=="/":
        if b == 0:
            print('ошибка, деление на ноль')
            break
        else:
            print(a/b)
            break
    if c=="+":
        print(a+b)
        break
    else:
        print("неправильный ввод")

# i=100
# for i in range(100, 0, -2):
#     print(i)

