def get_fibanaci(sum):
    sum = sum
    mass = [1, 1, 2]
    if sum == 1:
        mass = [1]
    elif sum == 2:
        mass = [1, 1]
    elif sum == 3:
        mass = [1, 1, 2]
    else:
        sum -= 3
        for i in range(1, sum + 1):
            count = mass[len(mass) - 1] + mass[len(mass) - 2]
            mass.append(count)
    return mass


num = int(input("Введите номер числа Фибаначи: "))
sad = get_fibanaci(num)
print(sad)
