import random

chislo = random.randint(1, 100)
otvet = False
att = 0
while otvet !=True:
    otvet_user = int(input('Введите число: '))
    if otvet_user == chislo:
        print('Вы угадали! Поздравляем! Количество попыток:', att)
        otvet = True
    elif otvet_user > chislo:
        print('-')
        att+=1
    elif otvet_user < chislo:
        print('+')
        att += 1
    
# изменение
