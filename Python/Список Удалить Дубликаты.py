mass = []
while True:
    num = input("Введите число или 'q' чтобы выйти: ")
    if num == 'q':
        break
    elif int(num) == float(num):
        mass.append(num)
    else:
        p = 0
print(mass)


# def get_dauble(mass):
#   while i <= len(mass):
#       if
#           i += 1
#       else:
#       for k in range(, (len(mass) - 1)):
#           print(k, mass[k])
#           if mass[i - 1] == mass[k - 1]:
#               mass.pop(k)
#   return mass
# def dedupe_v1(x):
#    y = []
#    for i in x:
#        if i not in y:
#            y.append(i)
#    return y
def dedupe_v1(x):
    return list(set(x))


print(dedupe_v1(mass))
