a = input('как дела?')
if a == "нормально":
    print('ok')
elif a == 'хорошо':
    print('отлично!')
elif a =='так себе':
    print('бывало и хуже')
else:
    print('почему?')
    b = input()
    if b == 'учёба' and a == 'плохо':
        print('Сочувствую')

