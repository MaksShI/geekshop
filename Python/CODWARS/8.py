def this(a, k):
    x = '1' + ('0' * (k - 1))
    x = int(x)
    mass = []
    y = x + x + 1000
    while x < y:
        if x % a == 0:
            mass.append(x)
        x += 1
    return mass


k = int(input('Введите сколько знаков должно содержать число: '))
a = int(input('Введите кратно чему оно должно быть: '))
print(this(a, k))
while True:
    if input('Введите любое слово и/или букву ,чтобы выйти из программы: ') != True:
        break
