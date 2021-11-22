import random

num = random.randint(0, 100)
coat = 8
k = 0
print("Для того чтобы угадать число у вас имеется", coat, "попыток")
while k != coat:
    k += 1
    player = int(input('Введите число от 0 до 100: '))
    if num > player:
        print("число слишком маленькое: ")
    elif num < player:
        print("число слишком большое: ")
    else:
        print("Вы угадали!!")
        break
print("Вы проиграли!")
