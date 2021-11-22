test = "Test this for my ex"
print(test)
stringLop = ""
test =[elem for elem in reversed(test)]
print(" ".join(test) )

def aboba(test):
    mass = []
    klon = []
    for i in test.split(" "):
        mass.append(i)
    k = len(mass)
    while len(mass) > 0:
        klon.append(mass[-1])
        mass.pop(-1)
    return str(klon)


rop = aboba(test)


# while rop != []: stringLop += a

def reverse(string):
    workstation = string.split()
    reverselist = [elem for elem in reversed(workstation)]
    reverselist = ' '.join(reverselist)
    return reverselist


while True:
    print(reverse(input('say something: ')))
    exit = input('"exit" to exit: ')
    if exit == 'exit':
        break
