n = input('Введите номер билета: ')
print(n)
a1 = int(n[0]) + int(n[1]) + int(n[2])
a2 = int(n[3]) + int(n[4]) + int(n[5])
if a1 == a2:
    print('Ура, Ваш билет счастливый!')
else:
    print('Увы, Ваш билет обычный.')