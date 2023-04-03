#### калькулятор 

def one(x,y):
    print(x+y)
    
def two(x,y):
    print(x-y)
    
def three(x,y):
    print(x*y)
    
def four(x,y):
    if y!=0:
        print(x/y)
    else:
        print('на ноль делить нельзя')
    


print('Это программа-калькулятор!') # вывод чего-то в консоль 

first_number = int(input('Введите первое число:')) # когда пользователь вводит что
                                                   #то с клавиатуры то это идет в офрмате str , а нам нужно в int 
operator = input('Введите оператор(+, -, *, :):\n')
second_number = int(input('Введите второе число:\n'))


if operator == '+': # ЕСЛИ переменная оператор ('+') == +
    one(first_number, second_number) # сложение 
elif operator == '-':
    two(first_number, second_number)
elif operator == '*':
    three(first_number, second_number)
elif operator == ':':
        four(first_number, second_number) # / - деление формата float и // - деление формата int 
    
else:
    print('Такого оператора нет в этой программе!')