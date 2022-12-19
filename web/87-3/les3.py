def sl_vich(a, b):
   summ = a + b
   vichit = a - b
   return summ, vichit

a = int(input("Введите первое число: "))
b = int(input('Введите второе число: '))

print(sl_vich(a, b))