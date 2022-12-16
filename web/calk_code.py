def summa(per_chisl, vtor_chisl, znac):
    if znac == '+':
        return per_chisl + vtor_chisl
    elif znac == '-':
        return per_chisl - vtor_chisl
    elif znac == '*':
        return per_chisl * vtor_chisl
    elif znac == '/':
        if vtor_chisl == 0:
            print('Деление на ноль запрещено!')
        else:
            return per_chisl / vtor_chisl
    elif znac == '//':
        return per_chisl // vtor_chisl
    elif znac == '%':
        return per_chisl % vtor_chisl
    elif znac == '**':
        return per_chisl ** vtor_chisl
    else:
        print('Вы ввели направильный знак!')


try:
    global pervoe_chislo, vtoroe_chislo
    while True:
        vopros = input('Начать работу калькулятора?').lower()
        if vopros == 'нет':
            break
        pervoe_chislo = int(input('Введите первое число: '))
        vtoroe_chislo = int(input('Введите второе число: '))
        znak = input('Введите знак: ')

        funk = summa(pervoe_chislo, vtoroe_chislo, znak)
        print(funk)
except (ValueError):
    print('Вы ввели буквы, а не цифры!')
except (SystemError):
    print('Ошибка системы!')
except (MemoryError):
    print('Недостаточно памяти для выполнения запроса')
