def sum_num(a, b):
    return a + b


def mass_sum(mass, num=0):
    if mass == []:
        return num
    else:
        num += mass[0]
        del mass[0]
        mass_sum(mass, num)


print(mass_sum([1, 2, 3, 4, 5, 25]))
# Алгоритм Дейкстры
# Алгоритм Беллмана Форда