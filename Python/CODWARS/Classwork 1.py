def fullname(age):
    age = str(age)
    mass = ['1', '2', '3', '4']
    if age == '11' or age == '12' or age == '13' or age == '14':
        return f'Вам {age} лет'
    elif age[-1] == '1':
        return f'Вам {age} год'
    elif age[-1] in mass:
        return f'Вам {age} года'
    return f'Вам {age} лет'


i = 0
while i != 99:
    print(fullname(i))
    i += 1
