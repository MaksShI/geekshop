from random import randint

numbers = randint(1000, 9999)
sum = []
print(numbers)
sum.append(numbers // 1000)
sum.append(numbers // 100 % 10)
sum.append(numbers // 10 % 10)
sum.append(numbers % 10)
while True:
    cows = 0
    buls = 0
    k = -1
    a = int(input('Введите 4-х значное число: '))
    mass = []
    mass.append(a // 1000)
    mass.append(a // 100 % 10)
    mass.append(a // 10 % 10)
    mass.append(a % 10)
    if a == numbers:
        print('Ты ПОБЕДИЛ!')
        break
    else:
        for i in mass:
            k += 1
            if i == numbers // 1000:
                if sum[k] == i:
                    cows += 1
                else:
                    buls += 1
            elif i == numbers // 100 % 10:
                if sum[k] == i:
                    cows += 1
                else:
                    buls += 1
            elif i == numbers // 10 % 10:
                if sum[k] == i:
                    cows += 1
                else:
                    buls += 1
            elif i == numbers % 10:
                if sum[k] == i:
                    cows += 1
                else:
                    buls += 1
            else:
                pass
    print(cows, '- cows', buls, '- buls')
