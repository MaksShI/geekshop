def knock(mass):
    k = 0
    for i in mass:
        if i == 0:
            mass.pop(k)
        k += 1
    return mass


def ones_counter(inp):
    s = 0
    mass = []
    if not 1 in inp:
        return []
    for i in inp:
        if i == 1:
            s += 1
        else:
            mass.append(s)
            s = 0
    mass.append(s)
    while 0 in mass:
        knock(mass)
    return mass


print(ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]))
