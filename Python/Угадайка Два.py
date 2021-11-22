from random import randint

i = randint(0, 100)
print(i)
k = 0
coat = 100
print('Игра угадай число , компютер будет угадывать ваше число! Число попыток -', coat)
a = randint(0, 100)
print(a)
while k != coat:
    k += 1
    x = input('Введите б-больше, или м-меньше, или !- победил: ')
    if x == 'б':
        a = a // 3 + a + 6
    elif x == 'м':
        a = a // 2 - 6
    elif k > 30:
        if x == 'б':
            a = a + 1
        else:
            a = a - 1
    else:
        break
    print(a)
print('Число попыток - ', k - 1)
print('Я победил!')