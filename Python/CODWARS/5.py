# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Определите строку.прототип.toAlternatingCase
# (или аналогичная функция/метод, например
# to_alternating_case/toAlternatingCase/ToAlternatingCase
# на выбранном вами языке; подробности см. в исходном решении)
# таким образом, чтобы каждая строчная буква становилась прописной,
# а каждая прописная буква становилась строчной. Например:

def to_alternating_case(string):
    mass = []
    k = 0
    alfa = ' { } , . / : ; ! @ $ % ^ & * ( ) - = + ? '
    alfa = alfa.split()
    string = ' '.join(string)
    string = string.split(' ')
    print(string)
    for i in string:

        if i in alfa:
            mass.append(i)
        elif i == '' and string[k+1] == '':
            mass.append(' ')
        elif i == i.upper():
            mass.append(i.lower())
        else:
            mass.append(i.upper())
        k += 1
    print(mass)
    return "".join(mass)


print(to_alternating_case('Hello World!'))
