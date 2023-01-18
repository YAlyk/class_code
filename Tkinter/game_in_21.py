koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
print('Поиграем в блэкджек?')
count = 0

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d.' %current)
        count += current
        if count > 21:
            print('Извините, но вы проиграли.')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'n':
        print('У вас %d очков и вы закончили игру.' %count)
        break

print('До новых встреч!')
